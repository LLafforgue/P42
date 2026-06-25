from __future__ import annotations
from abc import abstractmethod
import pygame

from .entities import Entity
from pacman.utils import Direction
from pacman.assets.asset_manager import AssetManager


class MovingEntity(Entity):
    # We don't use pixel per frame because of delta time.
    BASE_SPEED: float = 100.0  # Pixel per seconds, to override.
    ANIMATION_FRAMES: dict = {}

    def __init__(self, x: float, y: float, speed: float | None = None):
        super().__init__(x, y)
        self.speed: float = speed if speed is not None else self.BASE_SPEED
        # 2 directions so that if player press btn to change dir because it see
        # a path, if instant, player stop because there is still a wall.
        self.direction: Direction = Direction.NONE
        self.next_direction: Direction = Direction.NONE

        # To switch animations.
        self._animations: dict[
            tuple[str, Direction | None],
            tuple[pygame.Surface, ...]
        ] = {}
        self._anim_index: float = 0.0  # anim counters, adanced by fps * dt
        self._anim_fps: float = 8.0  # frames per second of anim

    # Load sprites, assign it to self._sprites for each directions, then
    # resize self.rect to match loaded frame dimensions.
    # NEED TO LOOK if we start load asset to init of Ghosts, and if we store
    # a different manager for each entity.
    def _load_assets(
            self, asset_manager: "AssetManager", asset_path: str) -> None:
        """
        Populate self._animations using asset_manager.
        Each subclass knows its own state model and file layout.
        """
        from pathlib import Path

        base_path = Path(asset_path)
        first_frames = None

        for anim, info in self.ANIMATION_FRAMES.items():
            full_path = base_path / info.get("subdir", ".") / info["filename"]
            frames = asset_manager.get_strip(
                full_path,
                frame_w=info["frame_w"],
                frame_h=info["frame_h"],
                frame_count=info["frame_count"],
                row=0,
                scale=info["scale"]
            )
            self._animations[anim] = frames

            if first_frames is None:
                first_frames = frames

        if first_frames:
            w, h = first_frames[0].get_size()
            self.rect = pygame.Rect(0, 0, w, h)
            self.rect.center = (round(self.x), round(self.y))

    @abstractmethod
    def _animation_key(self) -> tuple[str, Direction | None]:
        """
        Return the key into self._animations that matches the current
        entity state. Called every frame by current_frame.
        """
        return ("move", self.direction)

    # Need to take entity pixel pos, compare it into grid cell, check
    # the next cell at the direction, return False if wall.
    # We can also check the 2 corners of an entity rect in the movement
    # dir, not just the center, so that a large entity can't clip through
    # a gap.
    @abstractmethod
    def _can_move(self, direction: Direction) -> bool:
        """Return True if movement in direction is not blocked by a wall."""
        ...

    def move(self, dt: float) -> None:
        """Advance position along current direction, respecting maze walls."""
        # if can move for next dir, give direction the next direction
        if self._can_move(self.next_direction):
            self.direction = self.next_direction
        # if can move cur dir, calcul speed with dt with dir vector
        if self._can_move(self.direction):
            dx, dy = self.direction.get_vector()
            self.x += dx * self.speed * dt
            self.y += dy * self.speed * dt
        # Synchronize the rect every frames. To have good collisions check.
        # round is best than int to prevent taking always the lowest value.
        self.rect.center = (round(self.x), round(self.y))

    # To make animations smooth. Advancing anim index by anim fps * dt.
    # This is to have same visual speed for the animation cycle with any FPS.
    def _tick_animation(self, dt: float) -> None:
        key = self._animation_key()
        frames = self._animations.get(key, ())
        if frames:
            self._anim_index = (
                self._anim_index + self._anim_fps * dt
            ) % len(frames)

    # Look up the frame list for the curr dir in _animations.
    # None prevent crash if nothing is found.
    @property
    def current_frame(self) -> pygame.Surface | None:
        key = self._animation_key()
        frames = self._animations.get(key, ())
        if not frames:
            frames = next(iter(self._animations.values()), ())
        return frames[int(self._anim_index)] if frames else None
