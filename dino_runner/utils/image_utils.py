
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH


def get_centered_image(image_to_center, x_offset = 0, y_offset = 0):
    image = image_to_center
    rect = image.get_rect()
    rect.center = ((SCREEN_WIDTH // 2) + x_offset, (SCREEN_HEIGHT // 2) + y_offset)
    return image, rect
