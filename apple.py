import random
from coord import Coord


class Apple():
    def __init__(self, coord: Coord) -> None:
        self.coord = coord

    def change_pos(self, free_coords: list[Coord]):
        self.coord = free_coords[random.randint(0, len(free_coords) - 1)]
