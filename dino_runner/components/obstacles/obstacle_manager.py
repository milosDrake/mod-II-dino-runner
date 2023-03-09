import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import cactus
from dino_runner.components.obstacles.cactusLarge import CactusLarge
from dino_runner.utils.constants import BIRD, DEAD, HAMMER_TYPE, LARGE_CACTUS, SHIELD_TYPE, SMALL_CACTUS


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self):
            obstacle_types = {
               0: cactus(SMALL_CACTUS[0]),
               1: cactus(SMALL_CACTUS[1]),
               2: cactus(SMALL_CACTUS[2]),
               3: CactusLarge(LARGE_CACTUS[0]),
               4: CactusLarge(LARGE_CACTUS[1]),
               5: CactusLarge(LARGE_CACTUS[2]),
               6: Bird(BIRD[0])
            }
            return obstacle_types[random.randint(0, 6)]

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(self.generate_obstacle())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type == SHIELD_TYPE:
                    print('Shield activated, no damage recived')
                elif game.player.type == HAMMER_TYPE:
                    self.obstacles.pop()
                else:
                    game.player.image = DEAD
                    game.playing = False
                    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def remove_obstacles(self):
        self.obstacles = []
            