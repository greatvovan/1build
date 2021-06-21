import logging
import math
from dataclasses import dataclass
from .constants import Stud, Track, Drywall, ScrewCounts

HEIGHT = 96.0
logger = logging.getLogger(__name__)


@dataclass
class MaterialsList:
    track: float
    stud: int
    drywall: float
    screws_floor: int
    screws_ceiling: int
    screws_wall: int
    screws_panel: int

    def __eq__(self, other: 'MaterialsList'):
        float_compare_threshold = 0.01
        return self.stud == other.stud \
            and self.screws_floor == other.screws_floor \
            and self.screws_ceiling == other.screws_ceiling \
            and self.screws_wall == other.screws_wall \
            and self.screws_panel == other.screws_panel \
            and abs(self.track - other.track) <= float_compare_threshold \
            and abs(self.drywall - other.drywall) <= float_compare_threshold


def plan(length: float) -> MaterialsList:
    len_inch = length * 12
    logger.debug(f'plan: requested length = {length} ft ({len_inch} inches)')

    if len_inch < Stud.WIDTH * 2:
        raise ValueError('Length is too short')

    track_len = len_inch * 2
    stud_count = math.ceil(len_inch / (Drywall.WIDTH / 2) - 1.0) + 2  # One per half a panel plus two walls
    drywall_len = len_inch * 2
    floor_screws_count = max(ScrewCounts.MIN_FLOOR_SCREWS, int(len_inch / ScrewCounts.FLOOR_SCREW_INTERVAL) + 2)
    ceiling_screws_count = max(ScrewCounts.MIN_CEILING_SCREWS, int(len_inch / ScrewCounts.CEILING_SCREW_INTRVAL) + 2)
    wall_screw_count = ScrewCounts.SCREWS_PER_STUD_WALL * 2

    if len_inch <= Drywall.WIDTH:
        # The inner stud is the same as outer.
        panel_screw_count = stud_count * ScrewCounts.SCREWS_PER_STUD_PANEL * 2
    else:
        # Interior studs are different.
        panel_screw_count = (stud_count - 2) * ScrewCounts.SCREWS_PER_STUD_PANEL * 3 + \
                            2 * ScrewCounts.SCREWS_PER_STUD_PANEL * 2

    return MaterialsList(track_len / Track.LENGTH, stud_count, drywall_len / Drywall.WIDTH,
                         floor_screws_count, ceiling_screws_count, wall_screw_count, panel_screw_count)
