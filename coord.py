class Coord():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self, x_move: int, y_move: int):
        self.x += x_move
        self.y += y_move

    def __str__(self) -> str:
        return f"{self.x} {self.y}"

    def clone(self):
        return Coord(self.x, self.y)

    def __eq__(self, __o: object) -> bool:
        return __o.x == self.x and __o.y == self.y
