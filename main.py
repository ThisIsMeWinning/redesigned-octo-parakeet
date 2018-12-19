import pygame
import sys
import random
from noise import pnoise2
from pygame.locals import *

TILESIZE = 32
MAPWIDTH = 35
MAPHEIGHT = 25

# colors
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

resources = [DIRT, GRASS, WATER, COAL]

# dictionary for textures
textures = {
    DIRT: pygame.image.load('resources\dirt.png'),
    GRASS: pygame.image.load('resources\grass.png'),
    WATER: pygame.image.load('resources\water.png'),
    COAL: pygame.image.load('resources\coal.png')
}

PLAYER = pygame.image.load('resources\player.png')
playerPos = [0, 0]

tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

pygame.init()

DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
pygame.display.set_caption('2D Game')

for rw in range(MAPHEIGHT):
    for cl in range(MAPWIDTH):
        random.seed()
        randomNumber = random.randint(0,15)
        if randomNumber == 0:
            tile = COAL
        elif randomNumber == 1 or randomNumber == 2:
            tile = WATER
        elif randomNumber >= 3 and randomNumber <= 7:
            tile = GRASS
        else:
            tile = DIRT
        tilemap[rw][cl] = tile

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT and playerPos[0] < MAPWIDTH - 1:
                playerPos[0] += 1
            if event.key == K_LEFT and playerPos[0] > 0:
                playerPos[0] -= 1
            if event.key == K_UP and playerPos[1] > 0:
                playerPos[1] -= 1
            if event.key == K_DOWN and playerPos[1] < MAPHEIGHT - 1:
                playerPos[1] += 1

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAY.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
            DISPLAY.blit(PLAYER, (playerPos[0]*TILESIZE, playerPos[1]*TILESIZE))

    pygame.display.update()
