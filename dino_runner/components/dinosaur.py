import pygame
from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE, JUMPING, RUNNING, DUCKING, RUNNING_SHIELD, JUMPING_SHIELD, DUCKING_SHIELD
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    POWER_UP_TIME = 200

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
        self.type = DEFAULT_TYPE
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
        self.power_up_time = 0      

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

        self.power_up_time -= 1
        if self.power_up_time < 0:
            self.type = DEFAULT_TYPE    

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = self.run_img[self.type][0] if self.step < 5 else self.run_img[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS     

    def duck(self):
        self.image = self.duck_img[self.type][0] if self.step < 5 else self.duck_img[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS + 33
        self.state_duck = False

    def jump(self):
        self.image = self.jump_img[self.type]
        if self.jump_up:
            self.dino_rect.y -= 15
            if self.dino_rect.y <= 100:
                self.jump_up = False
        else:
            self.dino_rect.y += 15
            if self.dino_rect.y >= self.Y_POS:
                self.state_jump = False

    def activate_power_up(self, power_up_type):
        if power_up_type == SHIELD_TYPE:
            self.type = SHIELD_TYPE
            self.power_up_time = self.POWER_UP_TIME
