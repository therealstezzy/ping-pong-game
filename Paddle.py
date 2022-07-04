import pygame

class Paddle():
    PADDLE_WIDTH = 25
    PADDLE_LENGTH = 300
    PAD_SPEED = 3
    score = 0
    hit = 0

    def __init__(self, x, y, game): 
        self.pad = pygame.Rect(x, y, self.PADDLE_WIDTH, self.PADDLE_LENGTH)
        self.game = game

    def movement(self, keys_pressed):
        if keys_pressed[pygame.K_w] and self.pad.y > 0:
            self.pad.y -= self.PAD_SPEED
        if keys_pressed[pygame.K_s] and self.pad.y + self.pad.height < self.game.HEIGHT:
            self.pad.y += self.PAD_SPEED     
    
    def updateHit(self):
        self.hit += 1

class AI(Paddle):
    def __init__(self, x, y, game):
        super().__init__(x, y, game)

    def movement(self, keys_pressed):
        if keys_pressed[pygame.K_i] and self.pad.y > 0:
            self.pad.y -= self.PAD_SPEED
        if keys_pressed[pygame.K_k] and self.pad.y + self.pad.height < self.game.HEIGHT:
            self.pad.y += self.PAD_SPEED     
