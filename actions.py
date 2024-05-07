class Action:
    pass

#Sub-Class of Action
class EscapeAction(Action):
    pass


#Sub-Class of Action
class MovementAction(Action):
    def __init__(self,dx: int,dy: int) -> None:
        super().__init__()
        self.dx =dx
        self.dy = dy