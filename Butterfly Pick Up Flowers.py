import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("FlowerMeadow.jpg", 0, 0)
butterfly = tsk.Sprite("ButterflyGardener.png", 0, 0)

flowers = []
for i in range(30):
    flower = tsk.Sprite("SmallFlower.png", 0, 0)
    flower.center_x = random.randint(0, 1018)
    flower.center_y = random.randint(200, 550)
    flowers.append(flower)

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    butterfly.center = pygame.mouse.get_pos()
    flowers_to_destroy = []

    for flower in flowers:
        if pygame.sprite.collide_rect(butterfly, flower):
            print("Destroy flower!")
            flowers_to_destroy.append(flower)

    for flower in flowers_to_destroy:
        flowers.remove(flower)

    background.draw()
    for flower in flowers:
        flower.draw()
    butterfly.draw()

    pygame.display.flip()
    c.tick(30)
