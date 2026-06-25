from __future__ import annotations

from typing import TYPE_CHECKING
import pygame
import math

from pacman import ASSETS_DIR
from .base_screen import BaseScreen

if TYPE_CHECKING:
    from pacman.tmp_main import Engine


class MainMenu(BaseScreen):
    _ASSET_PATH = ASSETS_DIR / "menu" / "pacman_title.png"

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

        self.font_btn: pygame.font.Font | None = None

        raw = pygame.image.load(self._ASSET_PATH).convert_alpha()
        self._title_raw = raw

        self.title_surface: pygame.Surface | None = None

        self._glow_time: float = 0.0   # total elapsed seconds
        self._glow_alpha: int = 255   # current alpha for the title blit

        self.buttons = [
            ("START GAME", "game"),
            ("HIGHSCORES", "highscores"),
            ("INSTRUCTIONS", "instructions"),
            ("OPTIONS", "options"),
            ("EXIT", None),
        ]

        self.input_mode: str = "keyboard"
        self.selected: int = -1  # Btn selected (index)
        self.hovered: int | None = None

        self._last_size: tuple[int, int] | None = None
        self.title_rect: pygame.Rect | None = None
        self.line_rect: tuple[
            tuple[int, int],
            tuple[int, int],
            int
        ] | None = None
        self.btn_rects: list[pygame.Rect] = []

    def _btn_width_ratio(self, screen_w: int) -> float:
        """
        Button width ratio: 20% at 1920px, grows toward 40% on small screens.
        """
        REF_W = 1920
        MIN_RATIO = 0.20   # at 1920px (your preferred baseline)
        MAX_RATIO = 0.40   # cap on very small screens

        raw = MAX_RATIO - (MAX_RATIO - MIN_RATIO) * (screen_w / REF_W)
        return max(MIN_RATIO, min(MAX_RATIO, raw))

    def _btn_height_ratio(self, screen_font: int) -> float:
        """
        To calcul height ratio of buttons.

        Button height ratio: 100% at 1920px,
        grows toward 150% on small screens.
        """
        REF_W = 1920
        MIN_RATIO = 1.00   # at 1920px (your preferred baseline)
        MAX_RATIO = 1.50   # cap on very small screens

        raw = MAX_RATIO - (MAX_RATIO - MIN_RATIO) * (screen_font / REF_W)
        return max(MIN_RATIO, min(MAX_RATIO, raw))

    def _layout(self, surface: pygame.Surface) -> None:
        size = surface.get_size()
        if size == self._last_size:
            return
        self._last_size = size  # Size cache to not recompute everytime

        W, H = size
        cx = W // 2
        n = len(self.buttons)

        SEP_MARGIN = 10
        START_MARGIN = 0.04
        BOT_MARGIN = 0.02
        MARGINS = START_MARGIN + BOT_MARGIN

        # Width-driven title height
        REF_W = 1920  # 1920px reference
        raw_ratio = 1.0 - (1.0 - 0.65) * (W / REF_W)
        title_ratio = max(0.65, min(1.0, raw_ratio))

        orig_w, orig_h = self._title_raw.get_size()
        title_h_from_width = int(orig_h * (W * title_ratio / orig_w))

        # Height-driven title height cap (analytical)
        # total_h = title_h + SEP + H*MARGINS + title_h*0.1*(1.6*(n-1) + 1.3)
        # <= H => title_h * k <= H - SEP - H*MARGINS
        k = 1.0 + 0.1 * (1.6 * (n - 1) + 1.3)
        title_h_max = (H - SEP_MARGIN - H * MARGINS) / k

        # Pick the smaller of the two constraints
        title_h = max(1, min(title_h_from_width, int(title_h_max)))
        target_w = int(orig_w * (title_h / orig_h))

        # Commit title
        self.title_surface = pygame.transform.smoothscale(
            self._title_raw, (target_w, title_h)
        )
        self.title_rect = self.title_surface.get_rect(midtop=(cx, 0))

        # Derived button sizes
        btn_font_size = max(10, int(title_h * 0.1))
        self.font_btn = pygame.font.Font(None, btn_font_size)

        BTN_W = int(self._btn_width_ratio(W) * W)
        BTN_H = int(self._btn_height_ratio(H) * btn_font_size)
        BTN_GAP = int(1.6 * btn_font_size)

        l_y = title_h + SEP_MARGIN
        start_y = l_y + int(H * START_MARGIN)

        self.btn_rects = [
            pygame.Rect(cx - BTN_W // 2, start_y + i * BTN_GAP, BTN_W, BTN_H)
            for i in range(n)
        ]

    def _activate(self, index: int) -> None:
        """Activate the button at the given index."""
        _, target = self.buttons[index]
        if target is None:
            pygame.quit()
            raise SystemExit
        self.engine.set_state(target)

    def _hovered_index(self, pos: tuple[int, int]) -> int | None:
        """To get the index of the hovered button."""
        for i, rect in enumerate(self.btn_rects):
            if rect.collidepoint(pos):
                return i
        return None

    def handle_event(self, event: pygame.event.Event) -> None:
        # Keyboard navigation
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_DOWN, pygame.K_s):
                self.selected = (self.selected + 1) % len(self.buttons)
                self.input_mode = "keyboard"
            elif event.key in (pygame.K_UP, pygame.K_w):
                self.selected = (self.selected - 1) % len(self.buttons)
                self.input_mode = "keyboard"
            elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                self._activate(self.selected)

        # Mouse hover buttons
        elif event.type == pygame.MOUSEMOTION:
            self.hovered = self._hovered_index(event.pos)
            if self.hovered is not None:
                self.input_mode = "mouse"
                self.selected = self.hovered

        # Buttons mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked = self._hovered_index(event.pos)
            if clicked is not None:
                self._activate(clicked)

    def update(self, dt: float) -> None:
        # Title glow
        self._glow_time += dt
        sine = math.sin(self._glow_time * 2.0)   # ~2 Hz cycle
        self._glow_alpha = int(120 + (sine + 1) / 2 * 95)    # range 160–255

    def draw(self, surface: pygame.Surface) -> None:
        self._layout(surface)

        # Fill background
        surface.fill((0, 0, 0))

        # Draw title
        if self.title_surface and self.title_rect:
            self.title_surface.set_alpha(self._glow_alpha)
            surface.blit(self.title_surface, self.title_rect)

        # Draw buttons
        for i, rect in enumerate(self.btn_rects):
            # Selected button highlight
            is_highlighted = (
                i == self.selected if self.input_mode == "keyboard"
                else i == self.hovered
            )
            bg_color = (255, 215, 0) if is_highlighted else (30, 30, 60)
            txt_color = (10, 10, 26) if is_highlighted else (255, 215, 0)

            pygame.draw.rect(surface, bg_color, rect, border_radius=8)
            pygame.draw.rect(surface, (255, 215, 0), rect, 2, border_radius=8)

            btn_name, _ = self.buttons[i]
            if self.font_btn:
                btn_surf = self.font_btn.render(btn_name, True, txt_color)
                btn_rect = btn_surf.get_rect(center=rect.center)

            surface.blit(btn_surf, btn_rect)
