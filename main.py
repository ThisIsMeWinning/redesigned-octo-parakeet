import pygame
import sys
from pygame.locals import *

# colors
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

# dictionary for textures
textures = {
    DIRT: pygame.image.load('resources\dirt.png'),
    GRASS: pygame.image.load('resources\grass.png'),
    WATER: pygame.image.load('resources\water.png'),
    COAL: pygame.image.load('resources\coal.png')
}

tilemap = [
    [GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, WATER, WATER, WATER, GRASS],
    [GRASS, DIRT, WATER, WATER, GRASS],
    [GRASS, DIRT, COAL, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, DIRT]
]

TILESIZE = 32
MAPWIDTH = 5
MAPHEIGHT = 5

pygame.init()

DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
pygame.display.set_caption('2D Game')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAY.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

    pygame.display.update()
