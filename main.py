import tcod
from entity import Entity
from input_handlers import EventHandler
from actions import EscapeAction, MovementAction

def main():
    # print("Hello World!")
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet('./data/asset.png', 32,8,tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()
    #Add base entites
    player = Entity(int(screen_width/2), int(screen_height/2), '@', (255,255,255))
    npc = Entity(int(screen_width/2-5), int(screen_height/2), '@', (255,255,0))
    entites = {npc,player}

    with tcod.context.new_terminal(
        screen_width, 
        screen_height,
        tileset= tileset,
        title = "RogueLike",
        vsync = True,

        ) as context:
            root_console = tcod.console.Console(screen_width, screen_height, order = "F")


            #Main game loop
            while True:
                root_console.print(x=player.x,y=player.y, string = player.char, fg = player.color)
                # sroot_console.print(x=player.x,y=player.y, string = player.char, fg = player.color)
                
                context.present(root_console)
                #Clear previous frame 
                root_console.clear()
                for event in tcod.event.wait():
                #     if event.type == "QUIT":
                #          raise SystemExit()

                    action = event_handler.dispatch(event)                    
                    if action is None:
                        continue
                    if isinstance(action, MovementAction):
                        player.move(dx = action.dx, dy = action.dy)
                    elif isinstance(action, EscapeAction):
                        raise SystemExit()                    



if __name__ == "__main__":
    main()

