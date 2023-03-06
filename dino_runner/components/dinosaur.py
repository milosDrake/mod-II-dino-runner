import pygame
from dino_runner.utils.constants import JUMPING, RUNNING, DUCKING
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step = 0
        self.state_run = True
        self.state_duck = False
        self.state_jump = False
        self.jump_up = False

    def update(self, user_input):
        if user_input[pygame.K_DOWN]:
            self.state_duck = True
        elif user_input[pygame.K_UP]:
            self.state_jump = True 
            self.jump_up = True


        if self.state_jump:
            self.jump()
        elif self.state_duck:
            self.duck()
        else:
            self.run()
        
        self.step += 1
        if self.step == 10:
            self.step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS     

    def duck(self):
        self.image = DUCKING[0] if self.step < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS + 33
        self.state_duck = False

    def jump(self):
        self.image = JUMPING
        if self.jump_up:
            self.dino_rect.y -= 10
            if self.dino_rect.y <= 100:
                self.jump_up = False
        else:
            self.dino_rect.y += 10
            if self.dino_rect.y >= self.Y_POS:
                self.state_jump = False
