import pygame
from scripts.config import Config
config = Config()

class Block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Block, self).__init__()
        self.height = config.height/10
        self.width = config.width/10
        self.surf = pygame.Surface((self.height,self.width))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center=(
                config.width/10*x+self.width/2,
                config.height/10*y+self.height/2
            )
        )

blocks = pygame.sprite.Group()

def drawRoom(room):
    for i in range(1,len(room)):
        for ii in range(1,len(room[i])):
            if room[ii-1][i-1] == 1:
                new_block = Block(i,ii)
                blocks.add(new_block)


rooms = {
    "1": [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
}