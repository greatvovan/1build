import math
from .metal_stud.constants import Stud, Track, Drywall, ScrewNames
from .metal_stud.partition import MaterialsList


def format_measurable(mat_name: str, amount: float) -> str:
    return f'{mat_name.capitalize()}: {math.ceil(amount)} pcs ' \
           f'({(math.modf(amount)[0] or 1.0) * 100:0.0f}% of the last pc)'


def format_countable(mat_name: str, count: int):
    return f'{mat_name.capitalize()}: {count} pcs'


def format_list(ml: MaterialsList) -> str:
    lines = [
        "You'll need:",
        format_measurable(Track.NAME, ml.track),
        format_countable(Stud.NAME, ml.stud),
        format_measurable(Drywall.NAME, ml.drywall),
        format_countable(ScrewNames.FLOOR.value, ml.screws_floor),
        format_countable(ScrewNames.CEILING.value, ml.screws_ceiling),
        format_countable(ScrewNames.WALL.value, ml.screws_wall),
        format_countable(ScrewNames.PANEL.value, ml.screws_panel),
    ]

    return '\n'.join(lines)
