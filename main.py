import pygame
import sys
import random
import pickle
from pygame.locals import *

TILESIZE = 32
MAPWIDTH = 35
MAPHEIGHT = 25

# colors
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

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


def do_save():
    saveGame = open('save.txt', 'wb')
    saveValues = inventory
    pickle.dump(saveValues, saveGame)
    saveGame.close()

def do_load():
    loadGame = open('save.txt', 'rb')
    loadValues = pickle.load(loadGame)
    loadGame.close()

inventory = {
    DIRT: 0,
    GRASS: 0,
    WATER: 0,
    COAL: 0
}

PLAYER = pygame.image.load('resources\player.png')
playerPos = [0, 0]

tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

pygame.init()

INVFONT = pygame.font.Font('resources\cour.ttf', 18)

DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 50))
pygame.display.set_caption('2D Game')

for rw in range(MAPHEIGHT):
    for cl in range(MAPWIDTH):
        random.seed()
        randomNumber = random.randint(0, 15)
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
            do_save()
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

            if event.key == K_SPACE:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                inventory[currentTile] += 1
                tilemap[playerPos[1]][playerPos[0]] = DIRT

            if event.key == K_1:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[DIRT] > 0:
                    inventory[DIRT] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = DIRT
                    inventory[currentTile] += 1

            if event.key == K_2:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[GRASS] > 0:
                    inventory[GRASS] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = GRASS
                    inventory[currentTile] += 1

            if event.key == K_3:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[WATER] > 0:
                    inventory[WATER] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = WATER
                    inventory[currentTile] += 1

            if event.key == K_4:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[COAL] > 0:
                    inventory[COAL] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = COAL
                    inventory[currentTile] += 1

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAY.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
            DISPLAY.blit(PLAYER, (playerPos[0]*TILESIZE, playerPos[1]*TILESIZE))

    placePosition = 10
    for item in resources:
        DISPLAY.blit(textures[item], (placePosition, MAPHEIGHT*TILESIZE+20))
        placePosition += 20
        textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
        DISPLAY.blit(textObj, (placePosition, MAPHEIGHT*TILESIZE+20))
        placePosition += 50

    pygame.display.update()
