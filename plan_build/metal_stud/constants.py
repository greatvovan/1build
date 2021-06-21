from enum import Enum


class Stud:
    NAME = 'stud (8 ft)'
    LENGTH = 96.0
    THIKNESS = 3.0 + 5/8
    WIDTH = 1.0 + 1/4


class Track:
    NAME = 'track (10 ft)'
    LENGTH = 120.0
    THIKNESS = 3.0 + 5/8
    WIDTH = 1.0 + 1/4


class Drywall:
    NAME = 'drywall panel (4x8 ft)'
    HEIGHT = 96.0
    WIDTH = 48.0
    THIKNESS = 1/2


class ScrewNames(Enum):
    FLOOR = 'floor screws'
    CEILING = 'ceiling screws'
    WALL = 'wall screws'
    PANEL = 'panel screws'


class ScrewCounts:
    MIN_FLOOR_SCREWS = 2
    MIN_CEILING_SCREWS = 2
    SCREWS_PER_STUD_WALL = 7    # Depends on the building
    SCREWS_PER_STUD_PANEL = 9   # ~1 each foot, one side only
    FLOOR_SCREW_INTERVAL = 20
    CEILING_SCREW_INTRVAL = 20
