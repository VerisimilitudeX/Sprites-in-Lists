#### ---- SET UP ---- ####

# --- Libraries ---  #
import tsk
import pygame
pygame.init()

# --- Display variables --- #
window = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("Restaurant.jpg", 0, 0)

bread = tsk.Sprite("BreadSlice.png", 360, 420)
filenames = ["BreadSlice.png", "BurgerPatty.png", "CheeseSlice.png","HamSlice.png", "LettuceLeaf.png", "TomatoSlice.png"]
icons = []
ingredients = [bread]

# --- Icon creation loop --- #
for i in range(6):
    icon = tsk.Sprite(filenames[i], 0, 0)
    icon.scale = .55
    icon.x = 25 + 165 * i
    icon.center_y = 70
    icons.append(icon)

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # --- Mouse input --- #
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for icon in icons:
                if icon.rect.collidepoint(mouse_x, mouse_y):
                    layer = tsk.Sprite(icon.image, 0, 0)
                    layer.center_x = bread.center_x
                    layer.center_y = bread.center_y - len(ingredients * 20)
                    ingredients.append(layer)

    # --- Draw --- #
    background.draw()
    for sprite in icons:
        sprite.draw()
    for food in ingredients:
        food.draw()
    pygame.display.flip()
