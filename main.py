import pygame
from Game import *

def main():
    WIDTH = 1920
    LENGTH = 1000

    game = Game("Ping Pong", WIDTH, LENGTH)
    paddle = Paddle(25, LENGTH//2 , game) # 25, length//2
    paddle2 = Paddle(WIDTH - 50, LENGTH//2, game)
    ball = Ball(WIDTH//2, LENGTH//2, game)

    run = True
    while run:
        game.draw_window(paddle, paddle2, ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        keys_pressed = pygame.key.get_pressed()
        paddle.movement(keys_pressed)
        paddle2.movement(keys_pressed)
        ball.movement(paddle, paddle2)
        #ball.detect_movement(paddle, paddle2)

        

main()