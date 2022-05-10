"""
\\\\\\\\\\\\\\\\\\
LESSON: 5.4 - Sprites in a List
EXERCISE: Buried Treasure
\\\\\\\\\\\\\\\
"""

#### ---- SET UP ---- ####

# --- Libraries ---  #

# Set up tsk, pygame, and random libraries
import tsk
import pygame
import random
pygame.init()

# --- Variables --- #

# Open a 1018 x 573 window
window = pygame.display.set_mode([1018, 573])

# Create two sprites using "DugHole.jpg" and
# "Treasure.png", with the treasure in the hole
hole = tsk.Sprite("DugHole.jpg", 0, 0)
treasure = tsk.Sprite("Treasure.png", 0, 0)

# Create list for the dirt sprites
dirt_sprites = []

# --- Dirt sprite creation loop --- #

# For 30 repetitions, create a sprite using
# "DirtMound.png" at a random position in the bottom
# part of the screen, and add that sprite to the list
# ---> TEST AFTER THESE LINES <--- #
for i in range(30):
    mound = tsk.Sprite("DirtMound.png", random.randint(500, 1018), random.randint(500, 1018))
    dirt_sprites.append(mound)

#### ---- MAIN LOOP ---- ####

# Create a main loop
running = True
while running:

    # --- Event loop --- #

    # Create an event loop
    # ---> TEST AFTER THESE LINES <--- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        # --- Keyboard input --- #

        # When a key is pressed, check if there are
        # sprites left in the dirt list. If so, remove
        # the last dirt sprite from the list.
        # ---> TEST AFTER THESE LINES <--- #
        if tsk.get_key_pressed(pygame.K_LEFT):
            if mound in dirt_sprites:
                dirt_sprites.remove(mound)
#
    # --- Draw --- #

    # Draw the background and treasure sprites
    hole.draw()
    treasure.draw()
#
    # Use a loop to draw all the dirt sprites
    for dirt in dirt_sprites:
        dirt.draw()

    # Flip the display
    # ---> TEST AFTER THIS LINE <--- #
    pygame.display.flip()

#
#
# Turn in your Coding Exercise.
#