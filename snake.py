from constance import FIELD_SIZE
from coord import Coord
from direction import DOWN, LEFT, RIGHT, UP, Direction


class Snake():
    def __init__(self, coords: list[Coord], direction: Direction) -> None:
        self.coords = [i.clone() for i in coords]
        self.direction = direction

    def move(self):
        for i in reversed(range(len(self.coords)-1)):
            self.coords[i+1] = self.coords[i].clone()
        self.coords[0].move(self.direction.xy_move()[0],
                            self.direction.xy_move()[1])
        # moved_head = self.coords[0]

        # if moved_head.x >= FIELD_SIZE[0]:
        #     self.coords[0].move(-FIELD_SIZE[0], 0)
        #     self.direction = RIGHT
        # elif moved_head.x < 0:
        #     self.coords[0].move(FIELD_SIZE[0], 0)
        #     self.direction = LEFT
        # if moved_head.y >= FIELD_SIZE[1]:
        #     self.coords[0].move(0, -FIELD_SIZE[1])
        #     self.direction = UP
        # elif moved_head.y < 0:
        #     self.coords[0].move(0, FIELD_SIZE[1])
        #     self.direction = DOWN

    def change_direction(self, direction: Direction):
        if not self.direction.x_move == -1 * direction.x_move or (
           not self.direction.y_move == -1 * direction.y_move):
            self.direction = direction

    def append(self):
        self.coords.append(self.coords[-1].clone())

    def check_border_collision(self, head: Coord):
        x = head.x
        y = head.y
        return x < 0 or y < 0 or x >= FIELD_SIZE[0] or y >= FIELD_SIZE[1]
