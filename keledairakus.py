from typing import Optional, Tuple
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction

class KeledaiRakus(BaseLogic):
    def __init__(self):
        self.goal_position: Optional[Position] = None

    def manhattan_distance(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return abs(x1 - x2) + abs(y1 - y2)

    # parameter avoid_red untuk menghindari diamond merah
    def find_nearest_diamond(self, bot_position: Position, board: Board, avoid_red: bool = False) -> Optional[Position]:
        diamonds = [
            obj for obj in board.game_objects
            if obj.type == "DiamondGameObject"
            and not (avoid_red and obj.properties.points == 2)  # hindari merah jika diminta
        ]
        if not diamonds:
            return None

        best_diamond = None
        min_score = float('inf')
        for diamond in diamonds:
            distance = self.manhattan_distance(bot_position.x, bot_position.y, diamond.position.x, diamond.position.y)
            diamond_value = 2 if diamond.properties.points == 2 else 1
            score = distance / diamond_value
            if score < min_score:
                min_score = score
                best_diamond = diamond.position
        return best_diamond

    def is_safe_move(self, next_x: int, next_y: int, board: Board) -> bool:
        for obj in board.game_objects:
            if obj.type == "BotGameObject":
                distance = abs(obj.position.x - next_x) + abs(obj.position.y - next_y)
                if distance <= 2:
                    return False
        return True

    def next_move(self, board_bot: GameObject, board: Board) -> Tuple[int, int]:
        current_position = board_bot.position
        props = board_bot.properties

        # Jika diamond penuh, langsung pulang
        if props.diamonds >= 5:
            self.goal_position = props.base

        #  Jika diamond = 4, hindari diamond merah agar tidak overload
        elif props.diamonds >= 4:
            base_distance = self.manhattan_distance(current_position.x, current_position.y, props.base.x, props.base.y)
            nearest_diamond = self.find_nearest_diamond(current_position, board, avoid_red=True)  # ⛔ hindari merah
            diamond_distance = self.manhattan_distance(
                current_position.x, current_position.y,
                nearest_diamond.x, nearest_diamond.y
            ) if nearest_diamond else float('inf')
            self.goal_position = props.base if base_distance < diamond_distance else nearest_diamond

        #  Jika diamond < 4, cari diamond terbaik (boleh merah)
        else:
            self.goal_position = self.find_nearest_diamond(current_position, board)

        # Fallback jika tetap tidak ada target
        if not self.goal_position:
            self.goal_position = props.base

        # Hitung arah ke target
        delta_x, delta_y = get_direction(
            current_position.x, current_position.y,
            self.goal_position.x, self.goal_position.y
        )

        next_x, next_y = current_position.x + delta_x, current_position.y + delta_y

        # Jika langkah tidak aman, cari alternatif aman yang tetap mendekati goal
        if not self.is_safe_move(next_x, next_y, board):
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            safe_moves = []
            for dx, dy in directions:
                nx, ny = current_position.x + dx, current_position.y + dy
                if 0 <= nx < board.width and 0 <= ny < board.height and self.is_safe_move(nx, ny, board):
                    distance_to_goal = self.manhattan_distance(nx, ny, self.goal_position.x, self.goal_position.y)
                    safe_moves.append(((dx, dy), distance_to_goal))

            if safe_moves:
                safe_moves.sort(key=lambda item: item[1])
                return safe_moves[0][0]

            #  Jika semua arah bahaya, tetap maju ke goal
            return delta_x, delta_y

        return delta_x, delta_y
