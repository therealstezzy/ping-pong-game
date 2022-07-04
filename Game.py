import pygame
import neat
from Paddle import *
from Ball import *


pygame.font.init()
pygame.mixer.init()

class Game_Information():
    def __init__(self, left_hits, right_hits, left_score, right_score):
        self.left_hits = left_hits
        self.right_hits = right_hits
        self.left_score = left_score
        self.right_score = right_score
        
    

class Game():
    FPS = 60

    # Winning Text
    text= ""
    WINNER_FONT = pygame.font.SysFont('comicsans', 100)
    SCORE_FONT = pygame.font.SysFont('comicsans', 40)

    # Colors
    BLACK = (0,0,0)
    WHITE = (255, 255, 255)

    # Paddle and Ball

    def __init__(self, title, width, length):
        self.WIDTH = width
        self.LENGTH = length

        self.paddle = Paddle(25, self.LENGTH//2 , self) # 25, length//2
        self.paddle2 = AI(self.WIDTH - 50, self.LENGTH//2, self)
        self.ball = Ball(self.WIDTH//2, self.LENGTH//2, self)
        
        
        self.WIN = pygame.display.set_mode((self.WIDTH, self.LENGTH))
        pygame.display.set_caption(title)

    def display_winner(self):
        pygame.time.delay(5000)

    def draw_window(self):
        self.WIN.fill(self.BLACK)

        paddle_score = self.SCORE_FONT.render("Score: " + str(self.paddle.score), 1, self.WHITE)
        paddle_score2 = self.SCORE_FONT.render("Score: " + str(self.paddle2.score), 1, self.WHITE)
        self.WIN.blit(paddle_score, (10, 10))
        self.WIN.blit(paddle_score2, (self.WIDTH - paddle_score2.get_width() - 10, 10))

        pygame.draw.rect(self.WIN, self.WHITE, self.ball.ball)
        pygame.draw.rect(self.WIN, self.WHITE, self.paddle.pad)
        pygame.draw.rect(self.WIN, self.WHITE, self.paddle2.pad)
        pygame.display.update()

    def newRound(self):
        self.ball.ball.x = self.WIDTH//2
        self.ball.y = self.LENGTH//2
        self.direction_angle = 0
        self.VEL *= -1

        self.paddle.pad.x = 25
        self.paddle.pad.y = self.LENGTH//2

        self.paddle2.pad.x = self.WIDTH - 50
        self.paddle2.pad.y = self.LENGTH//2

    def test_paddle2(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw_window() # Draw everything
            keys_pressed = pygame.key.get_pressed()
            self.paddle.movement(keys_pressed)
            self.paddle2.movement(keys_pressed)
            self.ball.movement(self.paddle, self.paddle2)
    
    def train_ai(self, genome1, genome2, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)
        
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
           
            output1 = net1.activate((self.paddle.pad.y, self.ball.ball.y, abs(self.paddle.pad.x - self.ball.ball.x)))
            output2 = net2.activate((self.paddle2.pad.y, self.ball.ball.y, abs(self.paddle2.pad.x - self.paddle2.pad.x)))
            print(output1, output2)


            self.draw_window()
            
            self.ball.movement(self.paddle, self.paddle2)

            if self.paddle.score >= 1 or self.paddle2.score >= 1:
                self.calculate_fitness(genome1, genome2, game_info)
                break


    def calculate_fitness(self, genome1, genome2, game_info):
        pass


    def update_gameInfo(self):
        game_info = Game_Information(self.paddle.hit)

    def detect_events(self):
        if self.ball.ball.colliderect(self.paddle) or self.ball.ball.colliderect(self.paddle2.pad):
            pass
