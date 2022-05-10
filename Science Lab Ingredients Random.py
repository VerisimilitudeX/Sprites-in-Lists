"""
secondcode

Description:
"""

import tsk
import pygame
pygame.init()

window = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("ScienceLabWithShrinkRay.jpg", 0, 0)

bread = tsk.Sprite("FlowerPottedStem.png", 360, 420)
filenames = ["MilkCarton.png", "MooncakeBitten.png", "OrangeWedge.png","PizzaWhole.png"]
icons = []
ingredients = [bread]

for i in range(len(filenames) - 1):
    icon = tsk.Sprite(filenames[i], 0, 0)
    icon.scale = .55
    icon.x = 25 + 165 * i
    icon.center_y = 70
    icons.append(icon)

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for icon in icons:
                if icon.rect.collidepoint(mouse_x, mouse_y):
                    layer = tsk.Sprite(icon.image, 0, 0)
                    layer.center_x = bread.center_x
                    layer.center_y = bread.center_y - len(ingredients * 20)
                    ingredients.append(layer)
                icon.center_x += 10
    background.draw()
    for sprite in icons:
        sprite.draw()
    for food in ingredients:
        food.draw()
    pygame.display.flip()