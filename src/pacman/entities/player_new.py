from __future__ import annotations

import pygame
import os.path as pth
from pacman.utils import PacManConfig, PacmanErrors
from pacman.utils import Assets, Sprite, Wall
from .gums_new import GumManagerN
from .ghost import Ghost
from pacman.entities.moving_entities import MovingEntity
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pacman.ui.screens.game_view import GameView


class PlayerN(MovingEntity):
    """Represent the player (Pac-Man) in the maze."""

    def __init__(
            self,
            config: PacManConfig,
            game: GameView
            ) -> None:
        """Initialize the player with configuration and maze data.

        Args:
            config (PacManConfig): Game configuration object containing
                lives count and cell size.
            mazes (dict[str, list]): Dictionary mapping level keys to
                their grid representations.
        """
        self.__position: dict[str, tuple] = {
            "coord": (0, 0),
            "next_coord": (0, 0),
            "pixel": (0, 0),
        }
        self.__scores: dict = {
            'ghost': config.points_per_ghost,
            'gum': config.points_per_pacgum,
            'super_gum': config.points_per_superpacgum
        }
        self.__lives: int = config.lives
        self.__cells: int = config.cell_size
        self.__time: int = 0
        self.game_screen: GameView = game
        self.__mazes: dict[str, list] = game._maze_manager.grids
        self.__dirct: str = 'south'
        self.__move: bool = False
        self.__next_dirct: str | None = None
        self.__buffer_ttl: int = 0
        self.__frame_player_index: int = 0
        self.__sprites: dict[str, str] = {
            'north': Assets.PACMAN_UP,
            'south': Assets.PACMAN_DOWN,
            'east': Assets.PACMAN_RIGHT,
            'west': Assets.PACMAN_LEFT,
            'dark_north': Assets.DARK_PACMAN_UP,
            'dark_south': Assets.DARK_PACMAN_DOWN,
            'dark_east': Assets.DARK_PACMAN_RIGHT,
            'dark_west': Assets.DARK_PACMAN_LEFT}
        self.__scale: float = Sprite.PLAYER_DIM_SCALE / 100
        self.__score: int = 0
        self.__dark: int = 0
        self.__current_level: str = ""

    def _get_entitie_point(self, g_type: str) -> int:
        """Return the score value associated with an entitie type.

        Args:
            g_type (str): entitie type.

        Returns:
            int: Number of points awarded for collecting.

        Raises:
            PacmanErrors: If the entitie type is unsupported.
        """
        if g_type not in ['gum', 'super_gum', 'ghost']:
            raise PacmanErrors(
                'prog',
                'Not available key for points records',
                'player.py'
            )
        return self.__scores[g_type]

    def _chek_no_walls(
            self,
            level: str,
            orientation: str,
            coord: tuple[int, int] | None = None,
            mode: str = "std"
            ) -> bool:

        if level not in self.__mazes:
            raise PacmanErrors(
                'prog',
                f'{level} not a valid key',
                'player.py'
            )

        maze = self.__mazes[level]

        if coord is None:
            ln, col = self.position_to_coord()
        else:
            ln, col = coord

        ln = int(ln)
        col = int(col)

        cell_value = maze[ln][col]

        if mode == "std":

            if orientation == "north" and cell_value & Wall.NORD:
                return False

            if orientation == "south" and cell_value & Wall.SUD:
                return False

            if orientation == "east" and cell_value & Wall.EST:
                return False

            if orientation == "west" and cell_value & Wall.OUEST:
                return False

        return True

    def collision(self, entities: list, mode: str = "std") -> None:
        """"""
        self.ghost = []

        for entiti in entities:
            if isinstance(entiti, GumManagerN):
                gum_type = entiti.gum_in(self.__position['coord'])
                if gum_type:
                    self._set_score(self._get_entitie_point(gum_type))
                    if gum_type == 'super_gum':
                        self.__dark = Sprite.DARK_TEMP

            if isinstance(entiti, Ghost):
                if self._bounding_coll(tuple(entiti.rect[:3])):
                    if self.__dark == 0 and mode == 'std':
                        self.__move = False
                        self.reset()
                    else:
                        self._set_score(self._get_entitie_point('ghost'))

    def _bounding_coll(self, params_sprite2: tuple[int, int, int]) -> bool:

        dim_player = self._get_surface().get_size()[0]
        dim_ghost = params_sprite2[2]

        y1, x1 = self.__position['pixel']
        middle_y1 = y1 + self.__cells // 2
        middle_x1 = x1 + self.__cells // 2
        x2, y2 = params_sprite2[:2]
        middle_y2 = y2 + dim_ghost // 2
        middle_x2 = x2 + dim_ghost // 2
        self.ghost.append(params_sprite2)
        distance = (
            (middle_x2 - middle_x1)**2
            + (middle_y2 - middle_y1)**2
            )**0.5

        limite_dist = (dim_ghost + dim_player * self.__scale // 2) * 0.5

        if distance < limite_dist:
            # print("\033[1;31mCOLLISION\033[0m")
            return True

        return False

    def draw(self, display: pygame.Surface, blit: tuple) -> None:
        """Draw the player on the target surface.

        The sprite is rendered at its current pixel position, adjusted by the
        given display offset. A debug rectangle can also be drawn around the
        sprite's rendering area.

        Args:
            display (pygame.Surface):
            Target surface on which the player is drawn.
            blit (tuple[int, int]):
            Rendering offset applied to the player's screen position.
        """
        surface_srpite = self._get_surface()
        blit_pos = tuple(x + d for x, d in zip(self.get_pix_coord(), blit))
        display.blit(surface_srpite, blit_pos)
        # rect = surface_srpite.get_rect(topleft=blit_pos)
        # pygame.draw.rect(display, (150, 50, 20), rect, 1)

    def generate_surfaces(self, nbr_frame: int = 2
                          ) -> dict[str, list[pygame.Surface]]:
        """Load sprite sheets and slice them into per-direction frame lists.

        Args:
            nbr_frame (int): Number of animation frames to extract
                from each sprite sheet.
        Returns:
            dict[str, list[pygame.Surface]]: Mapping of direction names
                (``'north'``, ``'south'``, ``'east'``, ``'west'``) to
                their corresponding scaled frame surfaces.
        Raises:
            PacmanErrors: If a sprite sheet file is missing for any direction.
        """
        for key, path in self.__sprites.items():
            if not pth.isfile(path):
                raise PacmanErrors('Asset',
                                   f"No {path} available !",
                                   'player.py')
            image = pygame.image.load(path)

            frame_w = Sprite.PIXEL_ASSET_DIM
            frame_h = Sprite.PIXEL_ASSET_DIM

            def get_frame(img: pygame.Surface, index: int) -> pygame.Surface:
                rect = pygame.Rect(index * frame_w, 0, frame_w, frame_h)
                frame = pygame.Surface((frame_w, frame_h), pygame.SRCALPHA)
                frame.blit(img, (0, 0), rect)
                frame = pygame.transform.scale(
                        frame,
                        (
                            int(self.__cells * self.__scale),
                            int(self.__cells * self.__scale)
                        )
                    )
                sprite_rect = frame.get_rect()
                cell_surface = pygame.Surface((self.__cells, self.__cells),
                                              pygame.SRCALPHA)
                sprite_rect.center = cell_surface.get_rect().center
                cell_surface.blit(frame, sprite_rect)
                return cell_surface

            self.__sprites[key] = [get_frame(image, i)
                                   for i in range(nbr_frame)]
        return self.__sprites

    def _get_speed(self) -> int:

        speed_base: int = Sprite.SPEED_MOUV

        if self.__current_level != '' and int(self.__current_level) < 2:
            speed_base = int(Sprite.SPEED_MOUV * 0.75)

        if self.__dark:
            return int(speed_base * 1.33)

        return speed_base

    def move(self, dt: float, level: str | int, key: int = 0) -> None:

        if isinstance(level, int):
            level = str(level)

        moves = {
            "south": (1, 0), "north": (-1, 0),
            "west":  (0, -1), "east": (0, 1),
        }
        back_dir = {
            "south": "north", "north": "south",
            "west": "east",   "east": "west",
        }
        ortho_dir = {
            "south": ("east", "west"), "north": ("east", "west"),
            "west":  ("north", "south"), "east": ("north", "south"),
        }
        keys_directions = {
            pygame.K_DOWN:  "south", pygame.K_UP:   "north",
            pygame.K_LEFT:  "west",  pygame.K_RIGHT: "east",
        }

        speed = self._get_speed() * dt
        direction = keys_directions.get(key)
        is_back = direction == back_dir.get(self.__dirct)
        next_dir = direction and direction in ortho_dir.get(self.__dirct, ())

        # Enregistrement direction orthogonale souhaitée
        if next_dir:
            self.__next_dirct = direction
            self.__buffer_ttl = Sprite.BUFFER_TTL

        # Demi-tour hors cellule (toujours géométriquement valide)
        if not self._in_a_cell() and is_back:
            self.__dirct = direction
            self.__next_dirct = None
            self.__buffer_ttl = 0

        # Logique en cellule
        if self._in_a_cell():
            self._snap_to_cell()   # centrage précis

            if not self.__move:
                # Démarrage
                if direction and self._chek_no_walls(level, direction):
                    self.__dirct = direction
                    self.__move = True
            else:
                # Tentative de changement vers direction bufferisée
                if self.__next_dirct:
                    if self._chek_no_walls(level, self.__next_dirct):
                        self.__dirct = self.__next_dirct
                        self.__next_dirct = None
                        self.__buffer_ttl = 0
                    else:
                        self.__buffer_ttl -= 1
                        if self.__buffer_ttl <= 0:
                            self.__next_dirct = None

                # Vérification mur devant dans la direction courante
                if not self._chek_no_walls(level, self.__dirct):
                    self.__move = False

        # Déplacement avec clamp sur la prochaine cellule alignée
        if self.__move:
            dy, dx = moves[self.__dirct]
            py, px = self.__position["pixel"]
            new_py = py + dy * speed
            new_px = px + dx * speed

            # Cellule cible = prochaine dans la direction courante
            cur_row = round(py / self.__cells)
            cur_col = round(px / self.__cells)
            next_row = cur_row + dy
            next_col = cur_col + dx
            max_py = next_row * self.__cells
            max_px = next_col * self.__cells

            # Clamp : ne pas dépasser le centre de la prochaine cellule
            if dy > 0:
                new_py = min(new_py, max_py)
            if dy < 0:
                new_py = max(new_py, max_py)
            if dx > 0:
                new_px = min(new_px, max_px)
            if dx < 0:
                new_px = max(new_px, max_px)

            self.__position["pixel"] = (new_py, new_px)

    def update(self, dt: float) -> None:
        """"""
        game_current_level = self.game_screen._current_level
        if self.__current_level != game_current_level:
            self.__current_level = game_current_level
            self.reset()
        entities = [self.game_screen.gums, *self.game_screen.ghosts]
        self.collision(entities)
        self.__time += dt
        fpi = self.__frame_player_index

        if self.__dark > 0:
            self.__dark -= 1

        if self.__time >= Sprite.SPEED_ANIM / 20:
            fpi = (fpi + 1) % len(self.__sprites[self.__dirct])
            self.__time = 0
            self.__frame_player_index = fpi

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move(dt, level=game_current_level, key=pygame.K_RIGHT)

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(dt, level=game_current_level, key=pygame.K_DOWN)

        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(dt, level=game_current_level, key=pygame.K_UP)

        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move(dt, level=game_current_level, key=pygame.K_LEFT)
        else:
            self.move(dt, level=game_current_level)

    def _get_surface(self) -> pygame.Surface:
        """Return the currently displayed sprite frame.

        Selects the appropriate animation frame according to the player's
        current direction, animation index, and dark mode state.

        Returns:
            pygame.Surface: Surface corresponding to the current sprite frame.
        """
        dark = 'dark_' if self.__dark > 0 else ''
        return self.__sprites[dark + self.__dirct][self.__frame_player_index]

    def _set_lives(self) -> bool:
        """"""

    def _set_score(self, scored: int) -> None:
        """"""
        self.__score += scored

    def get_lives(self) -> int:
        """Return the current number of remaining lives.

        Returns:
            int: Number of lives left.
        """
        return self.__lives

    def _in_a_cell(self) -> bool:
        py, px = self.__position["pixel"]
        # Tolérance strictement inférieure à un pas de déplacement
        tolerance = (Sprite.SPEED_MOUV / 60) * 0.49   # < demi-pas
        target_py = round(py / self.__cells) * self.__cells
        target_px = round(px / self.__cells) * self.__cells
        return (abs(py - target_py) <= tolerance
                and abs(px - target_px) <= tolerance)

    def _snap_to_cell(self) -> None:
        py, px = self.__position["pixel"]
        row = round(py / self.__cells)
        col = round(px / self.__cells)
        self.__position["pixel"] = (
            float(row * self.__cells),
            float(col * self.__cells),
        )
        self.__position["coord"] = (row, col)

    def reset(self) -> None:
        """Place the player at the centre of the given level's grid.

        Searches outward from the geometric centre until a non-wall cell
        is found, then sets both ``coord`` and ``pixel`` accordingly.

        Args:
            level (str | int): Level key, as an integer or numeric string.
        """
        level = self.game_screen._current_level
        if isinstance(level, int):
            level = str(level)
        ln = len(self.__mazes[level]) // 2
        col = len(self.__mazes[level][0]) // 2

        while self.__mazes[level][ln][col] == 15:
            if self.__mazes[level][ln][col - 2] == 15:
                col -= 1
            else:
                col += 1
        self.__position["coord"] = (ln, col)
        self.__position["next_coord"] = (ln, col)
        self.__position["pixel"] = self.coord_to_position()

    def position_to_coord(
            self,
            pixel: tuple | None = None
            ) -> tuple[int, int]:

        if pixel is None:
            pixel = self.__position["pixel"]

        return (
            int(pixel[0] // self.__cells),
            int(pixel[1] // self.__cells),
        )

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
            return tuple(x * self.__cells
                         for x in self.__position["coord"])

        return tuple(x * self.__cells for x in coord)

    def get_pix_coord(self) -> tuple[int, int]:
        """Return the player's current pixel position as ``(x, y)`` for blit.

        Returns:
            tuple[int, int]: Pixel coordinates ``(col_px, row_px)`` suitable
                for passing directly to ``Surface.blit``.
        """
        return (self.__position["pixel"][1], self.__position["pixel"][0])

    def _animation_key(self):
        return super()._animation_key()

    def _can_move(self, direction):
        return super()._can_move(direction)
