import pygame
from ...utils import Assets
from .base_screen import BaseScreen
from pacman.entities import PlayerN

BG      = (34, 34, 38)
CYAN    = (64, 224, 255)
MAGENTA = (255, 64, 200)
YELLOW  = (255, 220, 40)
WHITE   = (245, 245, 245)


class HUD(BaseScreen):
    """
    HUD Pac-Man, ratio largeur:hauteur = 4:1.
    Dessine le cadre néon + LEVEL / SCORE / LIVES.
    """

    def __init__(self, width: int):
        self.width = width
        self.height = width // 4
        self.surface = pygame.Surface((self.width, self.height),
                                      pygame.SRCALPHA)

        self.font_label = pygame.font.SysFont("couriernew", 16, bold=True)
        self.font_value = pygame.font.SysFont("couriernew", 22, bold=True)

        pac_sheet = pygame.image.load(Assets.PACMAN_RIGHT).convert_alpha()
        half = pac_sheet.get_width() // 2
        life_raw = pac_sheet.subsurface((0, 0, half, pac_sheet.get_height()))
        icon_h = int(self.height * 0.32)
        icon_w = int(life_raw.get_width() * icon_h / life_raw.get_height())
        self.life_icon = pygame.transform.smoothscale(life_raw,
                                                      (icon_w, icon_h))

        self.zone_level_x = int(self.width * 0.02)
        self.zone_score_x = int(self.width * 0.34)
        self.zone_lives_x = int(self.width * 0.70)
        self.sep1_x = int(self.width * 0.32)
        self.sep2_x = int(self.width * 0.68)
        self._last_screen_size: tuple[int, int] | None = None

    def handle_event(self, event):
        """"""

    def update(self, dt):
        """"""

    def draw(self, surface):

        size = surface.get_size()
        if size == self._last_screen_size:
            return
        self._last_screen_size = size

        W, H = size
        cx = W // 2

        print(cx)
        print(size)
        ...

        rect = pygame.Rect(20, 50, 60, 40)
        hud = self.surface.blit(self.life_icon, (30, 30), rect)
        surface.blit(self.surface, (0, 0), hud)
        pygame.draw.rect(surface, (255, 0, 0), hud)

