import tsk
import pygame
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])

hole = tsk.Sprite("DugHole.jpg", 0, 0)
treasure = tsk.Sprite("Treasure.png", 0, 0)

dirt_sprites = []

for i in range(30):
    mound = tsk.Sprite("DirtMound.png", random.randint(500, 1018), random.randint(500, 1018))
    dirt_sprites.append(mound)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if tsk.get_key_pressed(pygame.K_LEFT):
            if mound in dirt_sprites:
                dirt_sprites.remove(mound)

    hole.draw()
    treasure.draw()

    for dirt in dirt_sprites:
        dirt.draw()

    pygame.display.flip()
