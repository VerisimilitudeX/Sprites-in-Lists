import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("OutdoorBushes.jpg", 0, 0)
bush = tsk.Sprite("Bush.png", 250, 280)
pandas = []

panda_spawn_time = 3000
panda_timer = 0

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    panda_timer += c.get_time()
    if panda_timer >= panda_spawn_time:
        panda_timer = 0
        panda = tsk.Sprite("Panda.png", -400, 150)
        pandas.append(panda)

    pandas_to_remove = []

    for panda in pandas:
        if panda.image == "Panda.png" and panda.center_x > 450:
            fancy_panda = tsk.Sprite("PandaGentleman.png", panda.x, panda.y + 10)
            pandas.append(fancy_panda)

            pandas_to_remove.append(panda)

    for panda in pandas_to_remove:
        pandas.remove(panda)

    for panda in pandas:
        panda.center_x += 0.15 * c.get_time()

    background.draw()
    for panda in pandas:
        panda.draw()
    bush.draw()

    c.tick(30)
    pygame.display.flip()
