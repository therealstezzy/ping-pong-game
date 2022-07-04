import pygame
from Game import *
from Paddle import *
from Ball import *
from AI import *
import neat
import os

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    config = neat.Config()

def main():
    WIDTH = 1920
    LENGTH = 1000

    game = Game("Ping Pong", WIDTH, LENGTH)
    paddle = Paddle(25, LENGTH//2 , game) # 25, length//2
    ai = AI(WIDTH - 50, LENGTH//2, game)
    ball = Ball(WIDTH//2, LENGTH//2, game)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        game.draw_window(paddle, ai, ball) # Draw everything
        keys_pressed = pygame.key.get_pressed()
        paddle.movement(keys_pressed)
        ai.movement(keys_pressed)
        ball.movement(paddle, ai)

main()