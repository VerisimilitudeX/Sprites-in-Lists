import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Space.jpg", 0, 0)
stars = []

for i in range(50):
    x = random.randint(0, 1000)
    y = random.randint(0, 550)
    star = tsk.Sprite("Star.png", x, y)
    stars.append(star)

fade_line = 1018

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    fade_line -= 0.16 * c.get_time()

    stars_to_remove = []
    for star in stars:
        if star.center_x > fade_line:
            stars_to_remove.append(star)
    for star in stars_to_remove:
        stars.remove(star)

    background.draw()
    for star in stars:
        star.draw()

    pygame.display.flip()
    c.tick(30)
