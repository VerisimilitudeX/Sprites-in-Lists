"""
LESSON: 5.4 - Sprites in Lists
EXERCISE: Code Your Own

TITLE: [Your Title Here]
DESCRIPTION: [Your Description Here]
"""

import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()
background = tsk.Sprite("NightSky.jpg", 0, 0)
spaceship = tsk.Sprite("RoundShip.png", 0, 0)
stars = []

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            star = tsk.Sprite("Star.png", 0, 0)
            star.center_x = x
            star.center_y = y
            stars.append(star)
    spaceship.center = pygame.mouse.get_pos()
    for star in stars:
        star.x += .5 * c.get_time()
        star.y += .3 * c.get_time()

    background.draw()
    for star in stars:
        star.draw()
    spaceship.draw()
    pygame.display.flip()
    c.tick(30)