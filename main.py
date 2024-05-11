import tcod
from entity import Entity
from input_handlers import EventHandler
from actions import EscapeAction, MovementAction
from engine import Engine

def main():
    # print("Hello World!")
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet('./data/asset.png', 32,8,tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()
    #Add base entites
    player = Entity(int(screen_width/2), int(screen_height/2), '@', (255,255,255))
    npc = Entity(int(screen_width/2-5), int(screen_height/2), '@', (255,255,0))
    entities = {npc,player}

    engine = Engine(entities=entities, event_handler=event_handler, player=player)



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
                engine.render(console=root_console, context = context)
                events = tcod.event.wait()
                engine.handle_events(events)

if __name__ == "__main__":
    main()

