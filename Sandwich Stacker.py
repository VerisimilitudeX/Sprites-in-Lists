"""
LESSON: 5.4 - Sprites in Lists
EXERCISE: Sandwich Stacker
"""

#### ---- SET UP ---- ####

# --- Libraries ---  #

# Import the tsk library
import tsk

# Import the pygame library
import pygame

# Initialize pygame
pygame.init()

# --- Display variables --- #

# Open a window of size [1018, 573], assign to window
window = pygame.display.set_mode([1018, 573])

# Create a SPRITE called background using
# "Restaurant.jpg" at (0, 0)
background = tsk.Sprite("Restaurant.jpg", 0, 0)

# Create a SPRITE called bread using "BreadSlice.png"
# at (360, 420)
bread = tsk.Sprite("BreadSlice.png", 360, 420)

# Create a list called filenames with these strings:
# BreadSlice.png, BurgerPatty.png, CheeseSlice.png,
# HamSlice.png, LettuceLeaf.png, TomatoSlice.png
filenames = ["BreadSlice.png", "BurgerPatty.png", "CheeseSlice.png","HamSlice.png", "LettuceLeaf.png", "TomatoSlice.png"]

# Create an empty list called icons
icons = []

# Create a list called ingredients that contains the
# bread sprite
ingredients = [bread]

# --- Icon creation loop --- #

# For i in range 6
for i in range(6):

    # Create a new SPRITE object called icon
    # using filenames[i] at the position (0, 0)
    icon = tsk.Sprite(filenames[i], 0, 0)

    # Set icon's SCALE to .55
    icon.scale = .55

    # Set the icon's X to 25 + 165 * i
    icon.x = 25 + 165 * i

    # Set the icon's CENTER_Y to 70
    icon.center_y = 70

    # Append icon to the icons list
    # ---> TEST AFTER THIS LINE <--- #
    icons.append(icon)

#### ---- MAIN LOOP ---- ####

# Create a variable called drawing and assign it True
drawing = True

# Loop while drawing
while drawing:

    # --- Event loop --- #

    # Create an event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # --- Mouse input --- #

        # Elif the event type is MOUSEBUTTONDOWN
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Store the mouse position in
            # mouse_x, mouse_y
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # For each icon sprite in the icons list
            for icon in icons:

                # If the icon overlaps with mouse_x and
                # mouse_y (using COLLIDEPOINT)
                if icon.rect.collidepoint(mouse_x, mouse_y):

                    # Create a SPRITE called layer
                    # using the icon's IMAGE at (0, 0)
                    layer = tsk.Sprite(icon.image, 0, 0)

                    # Set the layer's CENTER_X to the
                    # bread's CENTER_X
                    layer.center_x = bread.center_x

                    # Set the layer's CENTER_Y to the
                    # bread's CENTER_Y - the LENgth of
                    # ingredients * 20
                    layer.center_y = bread.center_y - len(ingredients * 20)

                    # APPEND the layer to ingredients
                    # ---> TEST AFTER THIS LINE <--- #
                    ingredients.append(layer)

    # --- Draw --- #

    # DRAW the background
    background.draw()

    # For each sprite in the icons list
    for sprite in icons:

        # DRAW sprite
        sprite.draw()

    # For each food in the ingredients list
    for food in ingredients:

        # DRAW food
        food.draw()

    # Flip the display
    # ---> TEST AFTER THIS LINE <--- #
    pygame.display.flip()
    
    
# Turn in your Coding Exercise.