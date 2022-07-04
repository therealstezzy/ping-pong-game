import pygame
pygame.font.init()
pygame.mixer.init()

class Game():
    FPS = 60

    # Winning Text
    text= ""
    WINNER_FONT = pygame.font.SysFont('comicsans', 100)
    SCORE_FONT = pygame.font.SysFont('comicsans', 40)

    # Colors
    BLACK = (0,0,0)
    WHITE = (255, 255, 255)

    def __init__(self, title, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(title)

    def display_winner(self):
        pygame.time.delay(5000)

    def draw_window(self, paddle, paddle2, ball):
        self.WIN.fill(self.BLACK)

        paddle_score = self.SCORE_FONT.render("Score: " + str(paddle.score), 1, self.WHITE)
        paddle_score2 = self.SCORE_FONT.render("Score: " + str(paddle2.score), 1, self.WHITE)
        self.WIN.blit(paddle_score, (10, 10))
        self.WIN.blit(paddle_score2, (self.WIDTH - paddle_score2.get_width() - 10, 10))

        pygame.draw.rect(self.WIN, self.WHITE, ball.ball)
        pygame.draw.rect(self.WIN, self.WHITE, paddle.pad)
        pygame.draw.rect(self.WIN, self.WHITE, paddle2.pad)
        pygame.display.update()

    def newRound(self, ball, paddle, paddle2):
        ball.ball.x = self.WIDTH//2
        ball.ball.y = self.HEIGHT//2
        ball.direction_angle = 0
        ball.VEL *= -1

        paddle.pad.x = 25
        paddle.pad.y = self.HEIGHT//2

        paddle2.pad.x = self.WIDTH - 50
        paddle2.pad.y = self.HEIGHT//2
