import pygame

FONT_STYLE = 'freesansbold.ttf'
BLACK_COLOR = (0, 0, 0)

def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 20)
    text = font.render(f"Points: {points}", True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (1000, 10)
    return text, text_rect