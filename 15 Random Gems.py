import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Desert.jpg", 0, 0)
gem_names = ["RoundGemBlue.png", "RoundGemRed.png", "RoundGemBrown.png", "RoundGemPink.png"]

gems = []

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

    for g in gems:
        g.draw()

    pygame.display.flip()

    c.tick(30)
