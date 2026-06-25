from enum import IntFlag, StrEnum, Enum


class Wall(IntFlag):
    """Bitmask representing the walls of a single maze cell."""
    NORD = 1 << 0
    EST = 1 << 1
    SUD = 1 << 2
    OUEST = 1 << 3


class Assets(StrEnum):
    """Bitmask representing the sprites of a single maze cell."""

    PACMAN_UP = 'src/pacman/assets/pacman/pac_man_up-sheet.png'
    DARK_PACMAN_UP = 'src/pacman/assets/pacman/dark_pac_man_up-sheet.png'
    PACMAN_DOWN = 'src/pacman/assets/pacman/pac_man_down-sheet.png'
    DARK_PACMAN_DOWN = 'src/pacman/assets/pacman/dark_pac_man_down-sheet.png'
    PACMAN_RIGHT = 'src/pacman/assets/pacman/pac_man_right-sheet.png'
    DARK_PACMAN_RIGHT = 'src/pacman/assets/pacman/dark_pac_man_right-sheet.png'
    PACMAN_LEFT = 'src/pacman/assets/pacman/pac_man_left-sheet.png'
    DARK_PACMAN_LEFT = 'src/pacman/assets/pacman/dark_pac_man_left-sheet.png'
    GUM = 'src/pacman/assets/gum/gums1-sheet.png'
    GHOST_PK_DOWN = "src/pacman/assets/ghost/ghost_pink_down_sheet.png"
    GHOST_PK_UP = "src/pacman/assets/ghost/ghost_pink_up_sheet.png"
    GHOST_PK_LEFT = "src/pacman/assets/ghost/ghost_pink_left_sheet.png"
    GHOST_PK_RIGHT = "src/pacman/assets/ghost/ghost_pink_right_sheet.png"


class Sprite(IntFlag):
    """Bitmask representing the sprites of a single maze cell."""
    PIXEL_ASSET_DIM = 48
    SPEED_ANIM = 5
    SPEED_MOUV = 250
    SPEED_MOUV_DARK = 275
    BUFFER_TTL = 2
    DARK_TEMP = 500
    PLAYER_DIM_SCALE = 75


class Direction(Enum):
    NONE = (0,  0)
    UP = (0, -1)
    DOWN = (0,  1)
    LEFT = (-1, 0)
    RIGHT = (1,  0)

    def get_vector(self) -> tuple[int, int]:
        return self.value

    def get_opposite(self) -> "Direction":
        if self is Direction.DOWN:
            return Direction.UP
        if self is Direction.UP:
            return Direction.DOWN
        if self is Direction.LEFT:
            return Direction.RIGHT
        if self is Direction.RIGHT:
            return Direction.LEFT
        return Direction.NONE


class GhostMode(Enum):
    CHASE = 1
    SCATTER = 2
    EDIBLE = 3
    EATEN = 4


class MazeConfig(IntFlag):
    PADDING = 10
    MARGIN = 20
