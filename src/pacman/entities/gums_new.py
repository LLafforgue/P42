from __future__ import annotations
import pygame
from pacman.utils import PacManConfig, PacmanErrors, Sprite, Assets
import os.path as pth
from .entities import Entity

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..ui.screens.game_view import GameView


class Gum:
    """Represent a collectible gum located in the maze.

    A gum occupies a single maze cell and can be either a regular gum
    or a super gum. Each gum keeps track of its grid coordinates,
    pixel position, activation state, and type.
    """
    gum_types = ['gum', 'super_gum']

    def __init__(self,
                 x: int,
                 y: int,
                 step: int) -> None:
        """Initialize a gum at the given maze coordinates.

        Args:
            x (int): Row index of the gum in the maze grid.
            y (int): Column index of the gum in the maze grid.
            step (int): Size of a maze cell in pixels.
        """
        self.__coord: tuple[int, int] = (x, y)

        def __initiate_pixel(x, y, step) -> tuple[int, int]:
            x_p = x * step
            y_p = y * step
            return (x_p, y_p)

        self.__pixel: tuple[int, int] = __initiate_pixel(x, y, step)
        self.__activate: bool = True
        self.__type: str = "gum"

    def deactivate(self) -> None:
        """Mark the gum as collected and remove it from the game."""
        self.__activate = False

    def get_state(self) -> bool:
        """Return whether the gum is still active.

        Returns:
            bool: ``True`` if the gum can still be collected,
                ``False`` otherwise.
        """
        return self.__activate

    def set_type(self, type_gum: str) -> None:
        """Set the gum type.

        Args:
            type_gum (str): Type of gum to assign. Must be either
                ``"gum"`` or ``"super_gum"``.

        Raises:
            PacmanErrors: If the provided gum type is unknown.
        """
        if type_gum in self.gum_types:
            self.__type = type_gum
        else:
            raise PacmanErrors('prog', "Unknown type of gum", "Gum")

    def get_coord(self) -> tuple[int, int]:
        """"""
        return self.__coord

    def get_type(self) -> str:
        """"""
        return self.__type

    def get_pix_coord(self) -> tuple[int, int]:
        """Return the player's current pixel position as ``(x, y)`` for blit.

        Returns:
            tuple[int, int]: Pixel coordinates ``(col_px, row_px)`` suitable
                for passing directly to ``Surface.blit``.
        """
        return (self.__pixel[1], self.__pixel[0])


class GumManagerN(Entity):
    """Represent the gums (Pac-Man) in the maze."""

    def __init__(
            self,
            config: PacManConfig,
            game: GameView
            ) -> None:
        """Initialize the GumManager with configuration and maze data.

        Args:
            config (PacManConfig): Game configuration object containing
                lives count and cell size.
            mazes (dict[str, list]): Dictionary mapping level keys to
                their grid representations.
        """
        self.game_screen: GameView = game
        self.__mazes: dict[str, list] = game._maze_manager.grids
        self.__scores: dict[str, int] = {
            'gum': config.points_per_pacgum,
            'super_gum': config.points_per_superpacgum
        }
        self.__frame_gum_index: int = 0
        self.__time: int = 0
        self.__step: int = config.cell_size
        self.__sprites: dict[str, str] = {'gum': Assets.GUM,
                                          'super_gum': Assets.GUM}
        self.__gum_map: list[list[Gum]] = []
        self._curent_level: int | str = ""

    def generate_gums(self, level: str | int) -> None:
        """Create all gums for the specified level.

        Gums are generated for every walkable maze cell. The first and last
        gums of the top and bottom rows are converted into super gums.

        Args:
            level (str | int): Level identifier.

        Raises:
            PacmanErrors: If the level does not exist in the maze data.
        """
        if isinstance(level, str | int):
            level = str(level)

        if level not in self.__mazes:
            raise PacmanErrors(
                'prog',
                f'{level} not a valid key',
                'gums.py'
                )
        maze = self.__mazes[level]
        i = 0
        for line in maze:
            new_gums = list(Gum(i, y, self.__step)
                            for y in range(0, len(line)) if line[y] != 15)
            if i == 0 or i == len(maze) - 1:
                new_gums[0].set_type('super_gum')
                new_gums[-1].set_type('super_gum')
            self.__gum_map.append(new_gums)
            i += 1

    def gum_in(self, coord: tuple[int, int]) -> str | None:
        """Collect the gum located at the specified coordinates.

        If an active gum exists at the given position, it is deactivated
        and its type is returned.
        """
        for line in self.__gum_map:
            for gum in line:
                if gum.get_coord() == coord and gum.get_state():
                    gum.deactivate()
                    return gum.get_type()

    def generate_surfaces(self, nbr_frame: int = 4
                          ) -> dict[str, list[pygame.Surface]]:
        """Load and prepare gum animation frames.

        Sprite sheets are loaded from disk and split into animation frames.
        Each frame is resized and centered within a maze cell.

        Args:
            nbr_frame (int, optional): Number of frames to extract from each
                sprite sheet. Defaults to ``4``.

        Returns:
            dict[str, list[pygame.Surface]]: Animation frames indexed by
                gum type.

        Raises:
            PacmanErrors: If a sprite sheet cannot be found.
        """
        frame_w = Sprite.PIXEL_ASSET_DIM
        frame_h = Sprite.PIXEL_ASSET_DIM

        def get_frame(img: pygame.Surface,
                      index: int,
                      type_g: str) -> pygame.Surface:
            """Extract and resize a frame from a gum sprite sheet.

            Args:
            img (pygame.Surface): Source sprite sheet.
            index (int): Frame index to extract.
            type_g (str): Gum type used to determine the scaling factor.

            Returns:
                pygame.Surface: Render-ready animation frame.
            """
            redim = self.__step // 4 if type_g == 'gum' else self.__step // 2
            rect = pygame.Rect(index * frame_w, 0, frame_w, frame_h)
            frame = pygame.Surface((frame_w, frame_h), pygame.SRCALPHA)
            frame.blit(img, (0, 0), rect)
            sprite_surface = pygame.transform.scale(
                frame,
                (redim, redim))
            sprite_rect = sprite_surface.get_rect()
            cell_surface = pygame.Surface(
                (self.__step, self.__step),
                pygame.SRCALPHA)
            sprite_rect.center = cell_surface.get_rect().center
            cell_surface.blit(sprite_surface, sprite_rect)
            return cell_surface

        for key, path in self.__sprites.items():
            if not pth.isfile(path):
                raise PacmanErrors('Asset',
                                   f"No {path} available !",
                                   'gums.py')
            image = pygame.image.load(path)

            self.__sprites[key] = [get_frame(image, i, key)
                                   for i in range(nbr_frame)]
        return self.__sprites

    def _get_rows(self, level: int | str) -> int:
        """Return the number of cols (height) for the given level.

        Args:
            level (int | str): Level index, as an integer or numeric string.

        Returns:
            int: Maze height expressed as a number of cells.

        Raises:
            PacmanErrors: If the level is absent from ``__mazes``.
        """
        if isinstance(level, int):
            level = str(level)
        if not self.__mazes.get(level):
            raise PacmanErrors(
                'prog',
                f'{level} not a valid key',
                'gums.py'
                )
        dim = self.__mazes[level]
        return dim['height']

    def _get_cols(self, level: int | str) -> int:
        """
        Return the number of columns (width) for the given level.

        Args:
            level (int | str): Level index, as an integer or numeric string.

        Returns:
            int: Maze width expressed as a number of cells.

        Raises:
            PacmanErrors: If the level is absent from ``__mazes``
        """
        if isinstance(level, int):
            level = str(level)
        if not self.__mazes.get(level):
            raise PacmanErrors(
                'prog',
                f'{level} not a valid key',
                'gums.py'
                )
        dim = self.__mazes[level]
        return dim['width']

    def update(self, dt: int) -> None:
        """"""
        current_level = self.game_screen._current_level
        if isinstance(current_level, int):
            current_level = str(current_level)
        if current_level != self._curent_level:
            self.__gum_map = []
            self.generate_gums(current_level)
            self._curent_level = current_level

        self.__time += dt
        fgi = self.__frame_gum_index
        if self.__time >= Sprite.SPEED_ANIM / 40:
            fgi = (
                self.__frame_gum_index + 1) % len(self.__sprites['gum'])
            self.__time = 0
            self.__frame_gum_index = fgi

    def draw(self, display: pygame.Surface, blit: tuple[int]) -> None:

        for line in self.__gum_map:
            for gum in line:
                if gum.get_state():
                    blit_position = tuple(
                        x + d for x, d in zip(gum.get_pix_coord(), blit))
                    if gum.get_type() == 'super_gum':
                        display.blit(
                            self.__sprites['super_gum'][
                                self.__frame_gum_index], blit_position)
                    else:
                        display.blit(
                            self.__sprites['gum'][
                                self.__frame_gum_index], blit_position)

    def collision(self, entities: list[tuple[int, int]], mode: str = "std"):
        """"""

    def _set_lives(self) -> bool:
        """"""

    def coord_to_position(self, coord: tuple | None = None) -> tuple[int, int]:
        """Convert grid coordinates to pixel coordinates.

        Args:
            coord (tuple | None): Grid coordinates ``(row, col)`` to convert.
                Defaults to ``None``, which uses the current player position.
        Returns:
            tuple[int, int]: Pixel coordinates ``(px_row, px_col)``
                corresponding to the top-left corner of the cell.
        """
        if coord is None:
            return tuple(x * self.__step + 20
                         for x in self.__position["coord"])

        return tuple(x * self.__step + 20 for x in coord)

    def get_surface(self) -> list[pygame.Surface]:
        """Return the animation frame list for the current direction.

        Returns:
            list[pygame.Surface]: Ordered list of surfaces representing
                each animation frame for the active direction.
        """
        return self.__sprites['gum']
