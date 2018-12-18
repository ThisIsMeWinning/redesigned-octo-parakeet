import pygame

background_color = (255, 255, 255)
(width, height) = (900, 600)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Charooga')
screen.fill(background_color)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

