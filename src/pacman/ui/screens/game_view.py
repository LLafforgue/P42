from __future__ import annotations

from typing import TYPE_CHECKING
import pygame

from pacman.maze_surface import MazeManager
from pacman.ui.screens.base_screen import BaseScreen

from pacman.entities import PlayerN
from pacman.entities import GumManagerN
from pacman.entities import Ghost
from pacman import ASSETS_DIR

from .hud import HUD

from pacman.assets.asset_manager import AssetManager

from pacman.entities.ai.random_ai import RandomAI

if TYPE_CHECKING:
    from pacman.tmp_main import Engine


class GameView(BaseScreen):
    _GHOST_PATH = ASSETS_DIR / "ghost"

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

        # Build and generate all maze grids once
        self._maze_manager = MazeManager(engine.config)
        self._maze_manager.generate_mazes()

        self._current_level: str = "0"
        self._maze_surface: pygame.Surface = self._maze_manager.get_surface(
            self._current_level
        )

        rows = self._maze_manager._get_rows(self._current_level)
        cols = self._maze_manager._get_cols(self._current_level)

        self.player: PlayerN = PlayerN(
            self.engine.config,
            self
            )
        self.player.generate_surfaces()
        self.player.reset()

        self.gums: GumManagerN = GumManagerN(
            self.engine.config,
            self
        )
        self.gums.generate_surfaces()

        self.ghost_spawn_points = [
            self._cell_to_pixel(0, 0),  # top-left
            self._cell_to_pixel(0, cols - 1),  # top-right
            self._cell_to_pixel(rows - 1, 0),  # bottom-left
            self._cell_to_pixel(rows - 1, cols - 1),  # bottom-right
        ]

        # Cached screen size to detect resize
        self._last_screen_size: tuple[int, int] | None = None
        self._blit_pos: tuple[int, int] = (0, 0)

        self.asset_manager: AssetManager = AssetManager()

        self.ghosts: list[Ghost] = [
            Ghost(x, y, (x, y), self._GHOST_PATH, self, ai=RandomAI)
            for x, y in self.ghost_spawn_points
        ]
        for ghost in self.ghosts:
            ghost._load_assets(self.asset_manager, self._GHOST_PATH)
            # ghost.generate_surfaces()

        self.hud: HUD = HUD(self._maze_surface.get_width())

    def _cell_to_pixel(self, row: int, col: int) -> tuple[int, int]:
        c_size = self._maze_manager.cell_size
        return (col * c_size + c_size / 2, row * c_size + c_size / 2)

    def _compute_layout(self, screen: pygame.Surface) -> None:
        """Recompute the blit position to center the maze on the screen."""
        size = screen.get_size()
        if size == self._last_screen_size:
            return
        self._last_screen_size = size

        sw, sh = size
        mw = self._maze_surface.get_width()
        mh = self._maze_surface.get_height()
        self._blit_pos = ((sw - mw) // 2, (sh - mh) // 2)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.engine.set_state("menu")

    # Need to include player, ghost ...
    def update(self, dt: float) -> None:
        self.gums.update(dt)
        self.player.update(dt)
        for ghost in self.ghosts:
            ghost.update(dt)

    def draw(self, surface: pygame.Surface) -> None:
        self._compute_layout(surface)
        surface.fill((0, 0, 0))

        self.hud.draw(surface)

        surface.blit(self._maze_surface, self._blit_pos)
        self.gums.draw(surface, self._blit_pos)
        self.player.draw(surface, self._blit_pos)
        for ghost in self.ghosts:
            ghost.draw(surface, self._blit_pos)
