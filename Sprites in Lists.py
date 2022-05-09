"""
LESSON: 5.4 - Sprites in Lists
WARMUP 4
"""

import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()
background = tsk.Sprite("Space.jpg", 0, 0)

stars = []

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            star = tsk.Sprite("ShootingStar.png", 0, 0)
            star.center_x = x
            star.center_y = y
            stars.append(star)

    # Move all stars here
    for star in stars:
        star.x += .5 * c.get_time()
        star.y += .3 * c.get_time()

    background.draw()
    for star in stars:
        star.draw()

    pygame.display.flip()
    c.tick(30)