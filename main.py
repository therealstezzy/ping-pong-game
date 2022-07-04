import pygame
from Game import *
from Paddle import *
from Ball import *
import neat
import os

def eval_genomes(genomes, config):
    width, height = 1920, 1000
    
    for i, (genome_id, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break
        
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[i+1:]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            game = Game("AI game", width, height)
            game.train_ai(genome1, genome2, config)



def run_neat(config):
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-27')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1)) # maybe every 5 generations

    winner = p.run(eval_genomes, 50)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    run_neat(config)



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

#main()