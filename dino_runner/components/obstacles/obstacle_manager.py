import random
import pygame
from dino_runner.components.obstacles.cactus import cactus
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_list = [
                cactus(SMALL_CACTUS[0]),
                cactus(SMALL_CACTUS[1]),
                cactus(SMALL_CACTUS[2])
                ]
            self.obstacles.append(cactus_list[random.randint(0, 2)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            