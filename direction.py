LEFT_STR = "LEFT"
RIGHT_STR = "RIGHT"
UP_STR = "UP"
DOWN_STR = "DOWN"


class Direction():
    def __init__(self, direction: str) -> None:
        self.direction = direction
        self.x_move = 0
        self.y_move = 0
        if direction == LEFT_STR:
            self.x_move = -1
        if direction == RIGHT_STR:
            self.x_move = 1
        if direction == UP_STR:
            self.y_move = 1
        if direction == DOWN_STR:
            self.y_move = -1

    def xy_move(self) -> tuple:
        return (self.x_move, self.y_move)


LEFT = Direction(LEFT_STR)
RIGHT = Direction(RIGHT_STR)
UP = Direction(UP_STR)
DOWN = Direction(DOWN_STR)
