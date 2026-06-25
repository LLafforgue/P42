from __future__ import annotations

from pacman.entities.ghost_ai import GhostAI
from pacman.utils.enums import Direction

from typing import TYPE_CHECKING
import random

if TYPE_CHECKING:
    from pacman.tmp_main import Engine
    from pacman.entities.ghost import Ghost
    from pacman.entities.player import Player


class RandomAI(GhostAI):
    ACTION_LIMITATIONS: dict[Direction, tuple[Direction]] = {
        Direction.UP: (Direction.DOWN,),
        Direction.DOWN: (Direction.UP,),
        Direction.LEFT: (Direction.RIGHT,),
        Direction.RIGHT: (Direction.LEFT,),
        Direction.NONE: ()
    }

    def choose_direction(
            self, ghost: Ghost,
            player: Player | None = None,
            engine: Engine | None = None
    ) -> Direction:
        limited_direction = self.ACTION_LIMITATIONS[ghost.direction]
        authorized = [
            direc for direc in Direction
            if direc not in limited_direction and direc != Direction.NONE
        ]

        for direc in random.sample(authorized, len(authorized)):
            if ghost._can_move(direc):
                return direc

        # If blocked, choose opposite dir
        return ghost.direction.get_opposite()
