"""
thirdcode

Description:
"""


import tsk
import pygame
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

floor = tsk.Sprite("WaterCity.jpg", 0, 0)
v_cat_speed = 0.06
h_cat_speed = 0.1
timer = 0

cats = []
vertical_cats = []

kitten = tsk.Sprite("MascotEagleIcon.png", 30, 250)
cats.append(kitten)

cat1 = tsk.Sprite("OtterStand.png", 100, 50)
cat2 = tsk.Sprite("OtterStand.png", 400, 50)
cat3 = tsk.Sprite("OtterStand.png", 700, 50)

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    at_edge = False

    if not pygame.sprite.collide_rect(cat1, kitten):
        cat1.center_x += v_cat_speed * c.get_time()
    if cat1.center_x > 573:
        cat1.center_x = 573
        at_edge = True
    if cat1.center_x < 150:
        cat1.center_x = 150
        at_edge = True

    if not pygame.sprite.collide_rect(cat2, kitten):
        cat2.center_x += v_cat_speed * c.get_time()
    if cat2.center_x > 573:
        cat2.center_x = 573
        at_edge = True
    if cat2.center_x < 150:
        cat2.center_x = 150
        at_edge = True

    if not pygame.sprite.collide_rect(cat3, kitten):
        cat3.center_x += v_cat_speed * c.get_time()
    if cat3.center_x > 573:
        cat3.center_x = 573
        at_edge = True
    if cat3.center_x < 150:
        cat3.center_x = 150
        at_edge = True

    if at_edge:
        v_cat_speed *= -1

    direction = 1
    if h_cat_speed < 0:
        direction = -1

    if timer >= 1000:
        h_cat_speed = random.randint(5, 20) * .01 * direction
        timer = 0

    kitten.center_x += h_cat_speed * c.get_time()

    if kitten.center_x > 1018:
        kitten.center_x = 1018
        h_cat_speed *= -1

    if kitten.center_x < 0:
       kitten.center_x = 0
       h_cat_speed *= -1

    if h_cat_speed > 0:
        kitten.flip_x = False
    else:
        kitten.flip_x = True

    cats_by_height = []
    while len(cats) > 0:

        min = 2000
        lowest_cat = ""

        for cat in cats:
            if cat.center_y < min:
                min = cat.center_y
                lowest_cat = cat

        cats.remove(lowest_cat)
        cats_by_height.append(lowest_cat)

    cats = cats_by_height

    floor.draw()

    cat1.draw()
    cat2.draw()
    cat3.draw()
    kitten.draw()

    pygame.display.flip()

    c.tick(30)
    timer += c.get_time()