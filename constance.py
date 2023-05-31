from coord import Coord
from direction import DOWN

INITIAL_POS = [Coord(6, 5), Coord(6, 6), Coord(6, 7)]
# INITIAL_POS = [Coord(0, 0), Coord(0, 1), Coord(0, 2)]
INITIAL_DIRECTION = DOWN
FIELD_SIZE = (14, 14)  # !change ind_size in genetic_alg.py when changing field size according to neural_network params quantity(you can see it in console("Total params"))
DELAY = 0.0014
CELL_SIZE = 50
MAX_SNAKE_SIZE = 40
