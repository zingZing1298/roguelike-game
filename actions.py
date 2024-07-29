from __future__ import annotations
from typing import Optional, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity
    

class Action:
    def __init__(self, engine:Engine, entity:Entity)-> None:
        super().__init__()
        self.entity = entity

    @property
    def engine(self)->Engine:
        return self.entity.gamemap.engine
    
    def perform(self) -> None:
        raise 

    
#Sub-Class of Action
class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()

class ActionWithDirection(Action):
    def __init__(self, dx:int, dy:int) -> None:
        super().__init__()
        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: Entity) -> None:
        raise NotImplementedError()

class MeleeAction(ActionWithDirection):

    def perform(self, engine:Engine, entity:Entity) -> None:
        dest_x = entity.x + self.x
        dest_y = entity.y + self.y

        target = engine.game_map.get_blocking_entity_at_location(dest_x,dest_y)
        if not target:
            return
        print(f"You kick the {target.name}, much to its annoyance")

class BumpAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.x
        dest_y = entity.y + self.y
        
        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return MeleeAction(self.dx, self.dy).perform(engine, entity)
        else:
            return MovementAction(self.dx, self.dy).perform(engine, entity)





#Sub-Class of Action
class MovementAction(ActionWithDirection):

    def perform(self, engine:Engine, entity:Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return 
        if not engine.game_map.tiles["walkable"][dest_x,dest_y]:
            return
        if engine.game_map.get_blocking_entity_at_location(dest_x,dest_y):
            return
        
        entity.move(self.dx,self.dy)
