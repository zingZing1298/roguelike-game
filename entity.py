from __future__ import annotations
import copy
from typing import Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from game_map import GameMap

T = TypeVar("T", bound = "Entity")

#Generic Entity object to represent players, enemies, items, etc.
class Entity:
    def __init__(
            self, 
            x: int = 0,
            y: int = 0, 
            char:str = '?', 
            color:Tuple[int,int,int] = (255,255,255),
            name: str ="<Unnamed>",
            blocks_movement: bool = False,) -> None:
        
        self.x = x
        self.y = y
        self.char  = char
        self.color = color
        self.name = name,
        self.blocks_movement = blocks_movement,

    #Automates the process of spawning entities by copying instance,and placing it a the passed location.
    def spawn(self:T, gamemap:GameMap, x:int, y:int) ->T:
        """
        Spawns a copy of this instace, at the given location(x,y).
        """
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        gamemap.entities.add(clone)
        return clone


    def move(self, dx:int, dy:int) -> None:
        self.x += dx
        self.y += dy