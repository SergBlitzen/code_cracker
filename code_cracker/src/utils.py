import random
from typing import Tuple, List

GRID_SIZE = 3


def initialize_grid(rows: int, columns: int) -> Tuple[Tuple[int, int]]:
    """
    Initializes main coordinates for grid.

    :param rows: Number of rows.
    :param columns: Number of columns.
    :return Tuple[Tuple[int]]: Tuple of coordinates in grid.
    """

    grid_list: List = []

    for i in range(rows):
        for j in range(columns):
            grid_list.append((i, j))

    grid = tuple(grid_list)
    return grid


def initialize_values(buttons_count: int) -> List[str]:
    """
    Initializes list with shuffled values for buttons.

    :param buttons_count: Count of
    :return List[str]: List of
    """

    values_list: List[str] = [str(num) for num in range(1, buttons_count + 1)]
    random.shuffle(values_list)
    return values_list


def get_button_coords(coords: Tuple[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Gets list of button grid coordinates."""

    return [x for x in coords if x[0] < 3 and x[1] < 3]


def get_correct_labels(coords: Tuple[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Gets list of correct labels grid coordinates."""

    return [x for x in coords if (x[0] > 2 and x[1] < 3) or (x[1] > 2 and x[0] < 3)]


def get_chosen_numbers():
    """Creates list of numbers to highlight."""

    numbers = [str(x) for x in range(1, 10)]
    return numbers


def get_check_coord() -> Tuple[int, int]:
    """Creates tuple for check button coordinates."""

    return GRID_SIZE, GRID_SIZE
