from __future__ import annotations

from pacman.entities.moving_entities import MovingEntity
from pacman.entities.ghost_ai import GhostAI
from pacman.utils.enums import GhostMode, Direction, Wall
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pacman.ui.screens.game_view import GameView

import pygame


GHOST_ANIMATION = {
    # --- Directional move animations ---
    ("move", Direction.LEFT):  {
        "subdir": ".",
        "frame_w": 48, "frame_h": 48, "frame_count": 3,
        "filename": "ghost_pink_left_sheet.png",
        "scale": None,
    },
    ("move", Direction.RIGHT): {
        "subdir": ".",
        "frame_w": 48, "frame_h": 48, "frame_count": 3,
        "filename": "ghost_pink_right_sheet.png",
        "scale": None,
    },
    ("move", Direction.UP): {
        "subdir": ".",
        "frame_w": 48, "frame_h": 48, "frame_count": 3,
        "filename": "ghost_pink_up_sheet.png",
        "scale": None,
    },
    ("move", Direction.DOWN): {
        "subdir": ".",
        "frame_w": 48, "frame_h": 48, "frame_count": 3,
        "filename": "ghost_pink_down_sheet.png",
        "scale": None,
    },
}


class Ghost(MovingEntity):
    ANIMATION_FRAMES = GHOST_ANIMATION

    def __init__(
            self,
            x: float,
            y: float,
            spawn: tuple[float, float],
            asset_path: str,
            game_screen: GameView,
            ai: GhostAI | None = None,
            speed: float | None = None,
    ) -> None:
        super().__init__(x, y, speed)
        self.mode: GhostMode = GhostMode.CHASE
        self.game_screen: GameView = game_screen
        self.spawn: tuple[float, float] = spawn
        self.last_cell_pos: tuple[int, int] = ()
        self.ai: GhostAI | None = ai() if ai else None
        self._edible_timer:  float = 0.0
        self._respawn_timer: float = 0.0

    def _can_move(self, direction: Direction) -> bool:
        maze_manager = self.game_screen._maze_manager
        cell_size = maze_manager.cell_size
        maze = maze_manager.grids[self.game_screen._current_level]
        level = self.game_screen._current_level

        rows = maze_manager._get_rows(level)
        cols = maze_manager._get_cols(level)

        # Current cell of ghost center
        col = int(self.x // cell_size)
        row = int(self.y // cell_size)
        col = max(0, min(cols - 1, col))
        row = max(0, min(rows - 1, row))

        # Check the wall on the current cell's face in the movement direction
        # and look if center was passed or not
        cell_val = maze[row][col]
        center_row = row * cell_size + cell_size / 2
        center_col = col * cell_size + cell_size / 2
        if direction == Direction.UP and self.y <= center_row:
            return not (cell_val & Wall.NORD)
        if direction == Direction.DOWN and self.y >= center_row:
            return not (cell_val & Wall.SUD)
        if direction == Direction.LEFT and self.x <= center_col:
            return not (cell_val & Wall.OUEST)
        if direction == Direction.RIGHT and self.x >= center_col:
            return not (cell_val & Wall.EST)
        return True

    def _animation_key(self) -> tuple[str, Direction | None]:
        if self.mode == GhostMode.SCATTER:
            # caller decides when to switch to flash based on _edible_timer
            return ("scatter", None)
        return ("move", self.direction)

    def _choose_direction(self) -> None:
        if self.ai:
            self.next_direction = self.ai.choose_direction(self)

    def update(self, dt: float) -> None:
        cell_size = self.game_screen._maze_manager.cell_size
        if not self.last_cell_pos:
            col = int(self.x // cell_size)
            row = int(self.y // cell_size)
            self.last_cell_pos = (col, row)

        # Ghost start with no dir, so we force to choose one
        if self.direction == Direction.NONE:
            self._choose_direction()

        self.move(dt)
        self._tick_animation(dt)

        # We check the cell pos after the move
        curr_col = int(self.x // cell_size)
        curr_row = int(self.y // cell_size)

        # Only pick a new direction when we attain the center of a new cell
        if curr_col != self.last_cell_pos[0] \
                or curr_row != self.last_cell_pos[1]:
            if self.direction in (Direction.UP, Direction.DOWN):
                center = curr_row * cell_size + cell_size / 2
                if (
                    (self.y <= center and self.direction is Direction.UP)
                    or (self.y > center and self.direction is Direction.DOWN)
                ):
                    self.y = center
                    self.x = round(self.x)
                    self.rect.center = (round(self.x), round(self.y))
                    self._choose_direction()
                    col = int(self.x // cell_size)
                    row = int(self.y // cell_size)
                    self.last_cell_pos = (col, row)
            else:
                center = curr_col * cell_size + cell_size / 2
                if (
                    (self.x >= center and self.direction is Direction.RIGHT)
                    or (self.x <= center and self.direction is Direction.LEFT)
                ):
                    self.x = center
                    self.y = round(self.y)
                    self.rect.center = (round(self.x), round(self.y))
                    self._choose_direction()
                    col = int(self.x // cell_size)
                    row = int(self.y // cell_size)
                    self.last_cell_pos = (col, row)

    def draw(self, surface: pygame.Surface,
             offset: tuple[int, int] = (0, 0)) -> None:
        frame = self.current_frame
        if frame:
            draw_rect = self.rect.move(offset[0], offset[1])
            surface.blit(frame, draw_rect)
            # pygame.draw.rect(surface, (255, 0, 0), draw_rect, 1)
