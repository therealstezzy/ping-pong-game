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

    def newRound(self):
        pass

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
    VEL = 5

    def __init__(self, x, y, game):
        self.ball = pygame.Rect(x, y, self.SIZE, self.SIZE)
        self.game = game

    def movement(self, paddle, paddle2):
        if self.ball.colliderect(paddle.pad)  or self.ball.colliderect(paddle2.pad):
            self.VEL *= -1

        if self.ball.x < 0:
            self.VEL *= -1
            self.game.newRound()
        
        if self.ball.x > self.game.WIDTH:
            self.VEL *= -1
            self.game.newRound()

        self.ball.x += self.VEL

    def bottom_hit():
        pass

    def top_hit():
        pass

    def middle_hit():
        pass
