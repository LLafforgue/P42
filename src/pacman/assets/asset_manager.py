from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import pygame


@dataclass(frozen=True)
class StripKey:
    path: str
    frame_w: int
    frame_h: int
    row: int
    frame_count: int
    scale: tuple[int, int] | None


class AssetManager:
    """
    Central cache for sprite sheets and prepared animation strips.

    Cache levels:
    - _sheets: raw loaded + alpha converted sprite sheets
    - _strips: extracted/copied/scaled frame tuples
    """

    def __init__(self) -> None:
        self._sheets: dict[str, pygame.Surface] = {}
        self._strips: dict[StripKey, tuple[pygame.Surface, ...]] = {}

    def load_sheet(self, path: str | Path) -> pygame.Surface:
        path = str(Path(path))
        # If no path cached, load it and convert alpha it, then store it.
        if path not in self._sheets:
            self._sheets[path] = pygame.image.load(path).convert_alpha()
        return self._sheets[path]

    def get_strip(
        self,
        path: str | Path,
        *,
        frame_w: int,
        frame_h: int,
        row: int,
        frame_count: int,
        scale: tuple[int, int] | None = None,
    ) -> tuple[pygame.Surface, ...]:
        # Create a StripKey to ensure correct caching of specific images
        key = StripKey(
            str(Path(path)), frame_w, frame_h, row, frame_count, scale)

        # Return cached strip
        if key in self._strips:
            return self._strips[key]

        sheet = self.load_sheet(key.path)
        frames: list[pygame.Surface] = []

        # For each frames, take it, by creating a Rect of same dim, and copy.
        for col in range(frame_count):
            rect = pygame.Rect(col * frame_w, row * frame_h, frame_w, frame_h)
            frame = sheet.subsurface(rect).copy()

            # Scale if needed
            if scale is not None and frame.get_size() != scale:
                frame = pygame.transform.scale(frame, scale)

            frames.append(frame)

        # Cache it
        result = tuple(frames)
        self._strips[key] = result
        return result

    def get_action_strips(
        self,
        directory: str | Path,
        *,
        frame_w: int,
        frame_h: int,
        frame_count: int,
        scale: tuple[int, int] | None = None,
        filenames: dict[str, str] | None = None,
    ) -> dict[str, tuple[pygame.Surface, ...]]:
        """
        Load one animated PNG per action.

        Example expected files in directory:
            right.png
            left.png
            up.png
            down.png

        Each file contains frame_count horizontal frames on row 0.
        """
        directory = Path(directory)

        result: dict[str, tuple[pygame.Surface, ...]] = {}
        if not filenames:
            raise ValueError("Need filenames to use get_action_strips.")

        for action_name, filename in filenames.items():
            result[action_name] = self.get_strip(
                directory / filename,
                frame_w=frame_w,
                frame_h=frame_h,
                row=0,
                frame_count=frame_count,
                scale=scale,
            )
        return result

    def clear(self) -> None:
        self._sheets.clear()
        self._strips.clear()


if __name__ == "__main__":
    from pacman import ASSETS_DIR
    pygame.init()
    pygame.display.set_mode((1, 1))

    try:
        path = ASSETS_DIR / "ghost"
        manager = AssetManager()

        strips_a = manager.get_action_strips(
            path,
            frame_w=48,
            frame_h=48,
            frame_count=3,
            scale=(32, 32),
            filenames={
                "LEFT": "ghost_pink_left_sheet.png",
                "UP": "ghost_pink_up_sheet.png",
                "RIGHT": "ghost_pink_right_sheet.png",
                "DOWN": "ghost_pink_down_sheet.png",
            }
        )
        strips_b = manager.get_action_strips(
            path,
            frame_w=48,
            frame_h=48,
            frame_count=3,
            scale=(32, 32),
            filenames={
                "LEFT": "ghost_pink_left_sheet.png",
                "UP": "ghost_pink_up_sheet.png",
                "RIGHT": "ghost_pink_right_sheet.png",
                "DOWN": "ghost_pink_down_sheet.png",
            }
        )

        print("cache hit on RIGHT strip:",
              strips_a["RIGHT"] is strips_b["RIGHT"])
        print("loaded directions:", list(strips_a.keys()))
        print("frames per direction:", {
            d: len(frames) for d, frames in strips_a.items()})
        print("frame sizes:", {
            d: [frame.get_size() for frame in frames]
            for d, frames in strips_a.items()
        })

        raw_right = manager.load_sheet(path / "ghost_pink_right_sheet.png")
        original_pixel = raw_right.get_at((0, 0))
        strips_a["RIGHT"][0].set_at((0, 0), (123, 45, 67, 255))

        print(
            "frame independent from source image:",
            manager.load_sheet(
                path / "ghost_pink_right_sheet.png"
            ).get_at((0, 0)) == original_pixel
        )
    except Exception as e:
        print(e)
    finally:
        pygame.quit()
