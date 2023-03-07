from dino_runner.components.obstacles.obstacle import obstacle

class cactus(obstacle):
    
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 325