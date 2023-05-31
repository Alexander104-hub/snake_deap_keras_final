import random
from time import sleep
from apple import Apple
from constance import DELAY, FIELD_SIZE, INITIAL_DIRECTION, INITIAL_POS
from coord import Coord
from direction import DOWN, LEFT, RIGHT, UP, Direction
from graphics import Graphics
from snake import Snake
from neural_network import NeuralNetwork


class SnakeEngine:
    def __init__(self) -> None:
        self.matrix = [Coord(i, j) for i in range(FIELD_SIZE[0])
                       for j in range(FIELD_SIZE[1])]
        self.neural_network = NeuralNetwork()

    def near_body_coords(self, snake: Snake) -> list[int]:
        coords = snake.coords[1:]
        head = snake.coords[0]
        near_coords = [1 for i in range(4)]
        #  Near body coords:
        for i in coords:
            if i.x == head.x + 1 and i.y == head.y:
                near_coords[0] = 0
            if i.x == head.x - 1 and i.y == head.y:
                near_coords[1] = 0
            if i.y == head.y - 1 and i.x == head.x:
                near_coords[2] = 0
            if i.y == head.y + 1 and i.x == head.x:
                near_coords[3] = 0
        return near_coords

    def near_coords(self, snake: Snake) -> list[int]:
        #  Возвращает список единиц и нулей. 1 если нет преграды. 0 если есть преграда.
        head = snake.coords[0]
        near_coords = self.near_body_coords(snake)
        #  Border coords:
        if head.x == 0:
            near_coords[1] = 0
        if head.y == 0:
            near_coords[2] = 0
        if head.x == FIELD_SIZE[0] - 1:
            near_coords[0] = 0
        if head.y == FIELD_SIZE[1] - 1:
            near_coords[3] = 0
        return near_coords

    def count_distance(self, coord1: Coord, coord2: Coord):
        return abs(coord1.x - coord2.x) + abs(coord1.y - coord2.y)

    def check_body_collision(self, coords: list[Coord]):
        return coords[0] in coords[1:]

    def check_border_collision(self, head: Coord):
        x = head.x
        y = head.y
        return x < 0 or y < 0 or x >= FIELD_SIZE[0] or y >= FIELD_SIZE[1]

    def play(self):
        displayable = random.randint(0, 500) % 50 == 0
        counter = 0
        snake = Snake(INITIAL_POS, INITIAL_DIRECTION)
        apple = Apple(Coord(-1, -1))
        apple.change_pos([coord for coord in self.matrix
                         if coord not in snake.coords])

        graphics = None
        #  Создание экрана
        if displayable:
            graphics = Graphics()
            graphics.restart(snake, apple, 0)
        score = 0
        reward = 0
        while True:
            head = snake.coords[0]
            near_coords = self.near_coords(snake)
            last_apple_distance = self.count_distance(apple.coord, snake.coords[0])

            applex_distance = apple.coord.x - head.x
            appley_distance = apple.coord.y - head.y

            if not applex_distance == 0:
                applex_distance = 1 if applex_distance > 0 else -1
            if not appley_distance == 0:
                appley_distance = 1 if appley_distance > 0 else -1
            #  Нейронная сеть определяет дальнейший ход змейки
            prediction = list(self.neural_network.predict(applex_distance,
                                                          appley_distance,
                                                          near_coords).numpy()[0])
            snake.change_direction([RIGHT, LEFT, UP, DOWN][prediction.index(max(prediction))])
            #  за съедание яблока даётся 500 очков
            if snake.coords[0] == apple.coord:
                apple.change_pos([coord for coord in self.matrix
                                  if coord not in snake.coords])
                counter -= 15
                reward += 500
                score += 1
                snake.append()
            #  5 процентов того, что игра будет показана на экране
            if displayable:
                graphics.update_display(snake=snake, apple=apple, score=score)
                sleep(DELAY)
            #  начисляется 25 очков за близкое прохождение около яблока
            if abs(apple.coord.x - head.x) + abs(apple.coord.y - head.y) == 1:
                reward += 25

            #  отнимается 1000 очков за поражение
            if self.check_body_collision(snake.coords) or self.check_border_collision(head):
                reward -= 1000
                if displayable:
                    graphics.set_game_over()
                    graphics.update_display(snake=snake, apple=apple, score=score)
                break
            if counter >= 150:
                break
            snake.move()
            #  отнимается 40 очков за отдаление от яблока
            if last_apple_distance < self.count_distance(apple.coord, snake.coords[0]):
                reward -= 40
            #  прибавляется 15 очков за приближение к яблоку
            if last_apple_distance > self.count_distance(apple.coord, snake.coords[0]):
                reward += 15
            counter += 1
        return reward,

    # Метод нужен для генетического алгоритма
    def evaluate(self, individual: list[int]):
        self.neural_network.set_weights(individual)
        reward = self.play()[0]

        for i in range(2):
            reward += self.play()[0] / 2
        return reward,
