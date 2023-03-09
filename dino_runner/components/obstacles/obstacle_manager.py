import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import cactus
from dino_runner.utils.constants import BIRD, DEAD, LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self):
            obstacle_types = {
               0: cactus(SMALL_CACTUS[0]),
               1: cactus(SMALL_CACTUS[1]),
               2: cactus(SMALL_CACTUS[2]),
               3: cactus(LARGE_CACTUS[0]),
               4: cactus(LARGE_CACTUS[1]),
               5: cactus(LARGE_CACTUS[2]),
               6: Bird(BIRD[0])
            }
            return obstacle_types[random.randint(5, 6)]

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(self.generate_obstacle())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.player.image = DEAD
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def remove_obstacles(self):
        self.obstacles = []
            