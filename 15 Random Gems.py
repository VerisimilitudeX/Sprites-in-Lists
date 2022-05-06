"""
LESSON: 5.4 - Sprites in Lists
WARMUP 1
"""
import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Desert.jpg", 0, 0)
gem_names = ["RoundGemBlue.png", "RoundGemRed.png", "RoundGemBrown.png", "RoundGemPink.png"]

# Create a list of gems
gems = []

# Create 15 random gems at random locations
for i in range(15):
    image = random.choice(gem_names)
    new_gem = tsk.Sprite(image, random.randint(0, 940), random.randint(50, 500))
    gems.append(new_gem)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    background.draw()

    # Draw all the gems
    for g in gems:
        g.draw()

    pygame.display.flip()

    c.tick(30)