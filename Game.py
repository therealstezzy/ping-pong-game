import pygame

class Game():
    FPS = 60

    # Winning Text

    # Colors
    BLACK = (0,0,0)
    WHITE = (255, 255, 255)

    def __init__(self, title, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(title)


    def draw_window(self, paddle, paddle2, ball):
        self.WIN.fill(self.BLACK)

        pygame.draw.rect(self.WIN, self.WHITE, ball.ball)
        pygame.draw.rect(self.WIN, self.WHITE, paddle.pad)
        pygame.draw.rect(self.WIN, self.WHITE, paddle2.pad)
        pygame.display.update()

class Paddle():
    PADDLE_WIDTH = 25
    PADDLE_LENGTH = 300
    PAD_SPEED = 5

    def __init__(self, x, y, game): 
        self.pad = pygame.Rect(x, y, self.PADDLE_WIDTH, self.PADDLE_LENGTH)
        self.game = game

    def movement(self, keys_pressed):
        if keys_pressed[pygame.K_w] and self.pad.y > 0:
            self.pad.y -= self.PAD_SPEED
        if keys_pressed[pygame.K_s] and self.pad.y + self.pad.height < self.game.HEIGHT:
            self.pad.y += self.PAD_SPEED      


class Ball():
    SIZE = 25

    def __init__(self, x, y, game):
        self.ball = pygame.Rect(x, y, self.SIZE, self.SIZE)

    def movement(self, paddle, paddle2):
        pass