from __future__ import annotations

from abc import ABC, abstractmethod
from pacman.utils.enums import Direction
# from .player import Player
# from .ghost import Ghost

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pacman.tmp_main import Engine
    from pacman.entities.player import Player
    from pacman.entities.ghost import Ghost


class GhostAI(ABC):

    ACTION_LIMITATIONS: dict = {}  # Filled with no autorized actions

    @abstractmethod
    def choose_direction(
        self,
        ghost: Ghost,
        player: Player | None = None,
        engine: Engine | None = None,
    ) -> Direction:
        ...
