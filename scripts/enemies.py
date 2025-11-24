#region ################# imports #################

import pygame
from scripts.config import Config
config = Config()
import random

#endregion ################# imports #################

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(config.height + 20, config.width + 100),
                random.randint(0, config.height),
            )
        )
        