"""
LESSON: 5.4 - Sprites in Lists
TECHNIQUE 4: Destroy Sprite
PRACTICE 1
"""
import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("ScienceLab.jpg", 0, 0)
robot = tsk.Sprite("FireBot.png", 0, 0)
fires = []

for i in range(100):
    x = random.randint(0, 852)
    y = random.randint(0, 369)
    file = random.choice(["SmallFire.png", "SmallFire2.png"])
    fire = tsk.Sprite(file, x, y)
    fires.append(fire)

drawing = True
while drawing:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Move Robot
    x, y = pygame.mouse.get_pos()
    robot.center = x, y

    # Remove fires that collide with Robot
    fires_to_remove = []
    for fire in fires:
        if pygame.sprite.collide_rect(fire, robot):
            fires_to_remove.append(fire)
    for fire in fires_to_remove:
        fires.remove(fire)

    # Draw
    background.draw()
    for fire in fires:
        fire.draw()
    robot.draw()

    pygame.display.flip()
    c.tick(30)


# Turn in your Coding Exercise.
