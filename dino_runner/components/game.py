import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power__up_manager import PowerUpManager
from dino_runner.utils.constants import BG, CLOUD, DINO_START, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.utils.image_utils import get_centered_image
from dino_runner.utils.tex_utils import get_centered_message, get_score_element


class Game:
    INITIAL_SPEED = 20

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.INITIAL_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.death_count = 0

    def show_score(self):
        self.points += 1

        if self.points % 50 == 0:
            self.game_speed += 1
            
        score, score_rect = get_score_element(self.points)
        self.screen.blit(score, score_rect)    

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(*get_centered_image(CLOUD, 100, 100))
        self.screen.blit(*get_centered_image(DINO_START, 0, -100))
        self.screen.blit(*get_centered_message('Press any kay to start!!'))
        self.screen.blit(*get_centered_message(f"Death Count: {self.death_count}", y_offset = 40, font_size= 20))
        pygame.display.update()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                print("Game Over")
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.run()    

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.time.delay(1000)    
        self.playing = False
        self.points = 0
        self.death_count += 1
        self.game_speed = self.INITIAL_SPEED
        self.obstacle_manager.remove_obstacles()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.show_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
