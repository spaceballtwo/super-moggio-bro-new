def on_up_pressed():
    if controller.A.is_pressed():
        mySprite.set_velocity(0, -75)
        controller.move_sprite(mySprite, 0, 0)
    else:
        pass
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_combos_attach_combo():
    controller.combos.set_trigger_type(TriggerType.CONTINUOUS)
    
    def on_debounce():
        if controller.A.is_pressed():
            mySprite.set_velocity(0, -70)
            
            def on_after():
                pass
            timer.after(750, on_after)
            
    timer.debounce("action", 500, on_debounce)
    
controller.combos.attach_combo("r + d", on_combos_attach_combo)

def on_player2_button_b_pressed():
    mysprite2.set_velocity(0, 50)
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player2_button_b_pressed)

def on_b_pressed():
    mySprite.set_velocity(0, 50)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    mySprite.set_velocity(0, -50)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_player2_button_a_pressed():
    mysprite2.set_velocity(0, -50)
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_player2_button_a_released():
    mysprite2.set_velocity(0, -30)
    pause(50)
    mysprite2.set_velocity(0, -20)
    pause(50)
    mysprite2.set_velocity(0, 0)
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.RELEASED,
    on_player2_button_a_released)

def on_player2_button_up_released():
    controller.player2.move_sprite(mysprite2, 50, 0)
controller.player2.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.RELEASED,
    on_player2_button_up_released)

def on_player2_button_up_pressed():
    if controller.A.is_pressed():
        mysprite2.set_velocity(0, -75)
        controller.player2.move_sprite(mysprite2, 0, 0)
    else:
        pass
controller.player2.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player2_button_up_pressed)

def on_a_released():
    mySprite.set_velocity(0, -30)
    pause(50)
    mySprite.set_velocity(0, -20)
    pause(50)
    mySprite.set_velocity(0, 0)
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def on_up_released():
    controller.move_sprite(mySprite, 50, 0)
    mySprite.set_velocity(0, -50)
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_player2_button_b_released():
    mysprite2.set_velocity(0, 30)
    pause(50)
    mysprite2.set_velocity(0, 20)
    pause(50)
    mysprite2.set_velocity(0, 0)
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.RELEASED,
    on_player2_button_b_released)

def on_b_released():
    mySprite.set_velocity(0, 30)
    pause(50)
    mySprite.set_velocity(0, 20)
    pause(50)
    mySprite.set_velocity(0, 0)
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

def on_combos_attach_combo2():
    controller.combos.set_trigger_type(TriggerType.CONTINUOUS)
    
    def on_debounce2():
        if controller.A.is_pressed():
            mySprite.set_velocity(0, -70)
    timer.debounce("action", 500, on_debounce2)
    
controller.combos.attach_combo("l + d", on_combos_attach_combo2)

def on_overlap_tile(sprite, location):
    pass
scene.on_overlap_tile(SpriteKind.player,
    sprites.castle.tile_grass1,
    on_overlap_tile)

mysprite2: Sprite = None
mySprite: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level6
"""))
tiles.set_current_tilemap(tilemap("""
    level2
"""))
mySprite = sprites.create(img("""
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    """),
    SpriteKind.player)
mysprite2 = sprites.create(img("""
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    """),
    SpriteKind.player)
tiles.place_on_tile(mySprite, tiles.get_tile_location(7, 63))
tiles.place_on_tile(mysprite2, tiles.get_tile_location(8, 63))
scene.camera_follow_sprite(mySprite)
controller.move_sprite(mySprite)
igt = 100
p2igt = 100
controller.player2.move_sprite(mysprite2, 50, 0)
splitScreen.camera_follow_sprite(splitScreen.Camera.CAMERA1, mySprite)
splitScreen.camera_follow_sprite(splitScreen.Camera.CAMERA2, mysprite2)
lap = 0
controller.combos.set_extended_combo_mode(True)

def on_update_interval():
    info.change_score_by(1)
    info.player2.change_score_by(1)
game.on_update_interval(10, on_update_interval)

def on_forever():
    global lap
    if mysprite2.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile
    """)):
        tiles.place_on_tile(mysprite2, tiles.get_tile_location(8, 63))
        lap += 1
        if lap == 3:
            game.game_over(True)
forever(on_forever)

def on_forever2():
    global lap
    if mySprite.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile
    """)):
        tiles.place_on_tile(mySprite, tiles.get_tile_location(7, 63))
        lap += 1
        if lap == 3:
            if info.score() < info.player2.score():
                game.game_over(True)
forever(on_forever2)

def on_forever3():
    if mysprite2.tile_kind_at(TileDirection.BOTTOM, sprites.castle.tile_grass1):
        if controller.A.is_pressed():
            mysprite2.set_velocity(0, -25)
        else:
            mysprite2.set_velocity(0, 0)
forever(on_forever3)

def on_forever4():
    if mySprite.tile_kind_at(TileDirection.BOTTOM, sprites.castle.tile_grass1):
        if controller.A.is_pressed():
            mySprite.set_velocity(0, -25)
        else:
            mySprite.set_velocity(0, 0)
forever(on_forever4)
