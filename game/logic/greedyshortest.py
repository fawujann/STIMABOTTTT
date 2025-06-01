from typing import Optional, Tuple
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction

class rakusjelek(BaseLogic):
    def __init__(self):
        self.goal_position: Optional[Position] = None

    def manhattan_distance(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return abs(x1 - x2) + abs(y1 - y2)

    def find_closest_diamond(self, bot_position: Position, board: Board) -> Optional[Position]:
        diamonds = [obj for obj in board.game_objects if obj.type == "DiamondGameObject"]
        if not diamonds:
            return None

        closest = min(diamonds, key=lambda d: self.manhattan_distance(
            bot_position.x, bot_position.y, d.position.x, d.position.y
        ))
        return closest.position

    def next_move(self, board_bot: GameObject, board: Board) -> Tuple[int, int]:
        current_position = board_bot.position
        props = board_bot.properties

        # Jika inventaris penuh, pulang ke base
        if props.diamonds >= 5:
            self.goal_position = props.base
        else:
            self.goal_position = self.find_closest_diamond(current_position, board)

        # Jika tidak ada target, kembali ke base
        if not self.goal_position:
            self.goal_position = props.base

        # Hitung arah ke target
        delta_x, delta_y = get_direction(
            current_position.x,
            current_position.y,
            self.goal_position.x,
            self.goal_position.y
        )

        return delta_x, delta_y
