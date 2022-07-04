import pygame
from Paddle import *

class AI(Paddle):
    def __init__(self, x, y, game):
        super().__init__(x, y, game)

    def movement(self, keys_pressed):
        if keys_pressed[pygame.K_i] and self.pad.y > 0:
            self.pad.y -= self.PAD_SPEED
        if keys_pressed[pygame.K_k] and self.pad.y + self.pad.height < self.game.HEIGHT:
            self.pad.y += self.PAD_SPEED     
