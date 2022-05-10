# Sprites-in-Lists
  # Why is it important to use a list when the program has many sprites?
    * Some programs have dozens or even hundreds of sprites
    * Making a separate variable for each sprite would take lots of redundant code
    * A list lets you store sprites without each one having its own variable
    * Lists should store sprites that all have similar behaviors
  # How to make a list of sprites
    * A sprite list is no different from any other list
    * You can start with an empty list [] and append sprites
    * You can declare a list that starts with sprites in it * Example: list = [sprite_a, sprite_b, sprite_c] * sprite_a, sprite_b, and sprite_c are all Sprite objects
  # How to draw many sprites at once
    * Group all the sprites you want to draw into a list
    * Iterate through the list with a for-each loop
    * Tell each of the sprites in the list to draw
    * Example: * for sprite in sprite_list: * sprite.draw()
    * Sprites draw in order * Later sprites in the list draw over earlier ones
    * Similar code can automate other sprite behaviors * Updating many animated sprites * Moving simultaneously * Checking many buttons for point collision
  # How to create many sprites at once
    * A for-range loop can create many sprites
    * Within the loop: * Declare a sprite * Add the sprite to a list
    * Normally, this would cause every sprite to have the same position and image
    * The sprites can be set to unique positions using the loop variable
    * Example: * i is the loop variable * The x coordinate of each sprite is set to i * 100 * The sprites will appear in a row, 100 pixels apart
    * A list of filenames can be used to create different images in one loop * A for-each loop can simply declare a Sprite for each filename * A for-range loop must index the list when declaring a Sprite * The advantage of the for-range loop is having the loop variable for positioning
