import tcod
from input_handlers import EventHandler
from actions import EscapeAction, MovementAction

def main():
    # print("Hello World!")
    screen_widht = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet('./data/asset.png', 32,8,tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()
    player_start_x = screen_widht//2
    player_start_y =screen_height//2

    with tcod.context.new_terminal(
        screen_widht, 
        screen_height,
        tileset= tileset,
        title = "RogueLike",
        vsync = True,

        ) as context:
            root_console = tcod.console.Console(screen_widht, screen_height, order = "F")


            #Main game loop
            while True:
                root_console.print(x=player_start_x,y=player_start_y, string = "@")
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
                        player_start_x += action.dx
                        player_start_y += action.dy

                    elif isinstance(action, EscapeAction):
                        raise SystemExit()                    



if __name__ == "__main__":
    main()

