import pygame

class Ball():
    SIZE = 25
    VEL = 3
    direction_angle = 0
    CHANGE_DIR = 0.5

    def __init__(self, x, y, game):
        self.ball = pygame.Rect(x, y, self.SIZE, self.SIZE)
        self.game = game

    def movement(self, paddle, paddle2):
        # touching paddle
        if self.ball.colliderect(paddle.pad) or self.ball.colliderect(paddle2.pad):
            self.VEL *= -1
            # middle
            if(self.ball.y < paddle.pad.y + 200 and self.ball.y > paddle.pad.y + 100):
                self.direction_angle -= self.CHANGE_DIR
            
            # top
            if(self.ball.y < paddle.pad.y + 100 and self.ball.y > paddle.pad.y - 1):
                self.direction_angle += (self.CHANGE_DIR * -1)

            # bottom
            if(self.ball.y < paddle.pad.y + 300 and self.ball.y > paddle.pad.y + 200):
                self.direction_angle += self.CHANGE_DIR

        # touching border [top and bottom]
        if self.ball.y < 0:
            self.direction_angle *= -1
            self.VEL *= -1

        if self.ball.y > self.game.HEIGHT:
            self.direction_angle *= -1
        
        # touching border [left and right]
        if self.ball.x < 0:
            paddle2.score += 1
            self.game.newRound(self, paddle, paddle2)
        
        if self.ball.x > self.game.WIDTH:
            paddle.score += 1
            self.game.newRound(self, paddle, paddle2)

        
        if self.ball.y < 0:
            self.VEL *= -1

        self.ball.x += self.VEL
        self.ball.y += self.direction_angle