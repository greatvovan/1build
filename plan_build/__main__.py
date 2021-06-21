import sys
from .metal_stud.partition import plan
from .utils import format_list
from .metal_stud.constants import Stud


def main():
    try:
        length = float(sys.argv[1])
    except (IndexError, ValueError):
        print(f'Usage: python -m {sys.argv[0].split("/")[-2]} <float length in ft>')
        return

    try:
        validate(length)
    except ValueError as e:
        print(e)
        return

    materials_list = plan(length)
    print(format_list(materials_list))


def validate(length: float):
    if length < 0.0:
        raise ValueError('Kernel panic. Core dumped.')

    if length == 0.0:
        raise ValueError('You are done! Congratulations!')

    if length * 12 < Stud.WIDTH * 2:
        raise ValueError('The wall is too short. Are you sure you need it?')


main()
