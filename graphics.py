import pygame
from apple import Apple
from constance import CELL_SIZE, FIELD_SIZE
from snake import Snake

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (6, 139, 0)
grey = (128, 128, 128)
body_color = (255, 100, 0)
head_color = (255, 147, 1)

DIS_WIDTH = CELL_SIZE * (FIELD_SIZE[0])
DIS_HEIGHT = CELL_SIZE * (FIELD_SIZE[1] + 0.5)


class Graphics():
    def __init__(self) -> None:
        pygame.init()

        # Set up the screen
        self.dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
        print('FFFFF\n\nFFFFF\n\nFFFFF')
        pygame.display.set_caption('Snake Game')
        self.dis.fill(green)

        self.game_over = False

        # Load Images
        apple_img = pygame.image.load("res/apple.png").convert_alpha()
        self.apple_img = pygame.transform.scale(apple_img, (CELL_SIZE-1, CELL_SIZE-1))
        snake_head_img = pygame.image.load("res/snake_head.png").convert_alpha()
        self.snake_head_img = pygame.transform.scale(snake_head_img, (CELL_SIZE, CELL_SIZE))
        snake_body_img = pygame.image.load("res/snake_body.png").convert_alpha()
        self.snake_body_img = pygame.transform.scale(snake_body_img, (CELL_SIZE, CELL_SIZE))

        pygame.display.update()

    def restart(self, snake: Snake, apple: Apple, score: int):
        self.update_display(snake, apple, score)

    def set_game_over(self):
        self.game_over = True

    def update_display(self, snake: Snake, apple: Apple, score: int):
        self.dis.fill(green)
        snake_coords = snake.coords

        #  Draw apple
        self.dis.blit(self.apple_img, (apple.coord.x * CELL_SIZE,
                      (apple.coord.y + 0.5) * CELL_SIZE))
        #  Draw head
        angle = (1 if (snake_coords[0].x - snake_coords[1].x) < 0 else 0) * 180 + (snake_coords[0].y - snake_coords[1].y) * (-90)
        if abs(snake_coords[0].x - snake_coords[1].x) + abs(snake_coords[0].y - snake_coords[1].y) > 1:
            angle = (0 if snake.direction.x_move > 0 else 1) * 180 + snake.direction.y_move * 90

        snake_head_img = pygame.transform.rotate(self.snake_head_img, angle)
        self.dis.blit(snake_head_img, (snake_coords[0].x * CELL_SIZE,
                      (snake_coords[0].y + 0.5) * CELL_SIZE))

        #  Draw body:
        for i in range(len(snake_coords[1:])):
            self.dis.blit(self.snake_body_img, (snake_coords[i+1].x * CELL_SIZE,
                          (snake_coords[i+1].y + 0.5) * CELL_SIZE))

        pygame.draw.rect(self.dis, white,
                         [0, 0, DIS_WIDTH, CELL_SIZE*0.5])

        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, black, white)
        textRect = text.get_rect()
        textRect.center = (text.get_rect().size[0] / 2, text.get_rect().size[1] / 2)
        self.dis.blit(text, textRect)

        if self.game_over:
            font = pygame.font.Font(None, FIELD_SIZE[0] * 6)
            text = font.render('GAME OVER', True, red)
            textRect = text.get_rect()
            textRect.center = (FIELD_SIZE[0] * CELL_SIZE / 2, 
                               FIELD_SIZE[1] * CELL_SIZE / 2)
            self.dis.blit(text, textRect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
