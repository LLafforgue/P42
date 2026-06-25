from __future__ import annotations
from abc import ABC, abstractmethod
import pygame


class Entity(ABC):
    """
    Root base class for every object that exists in the maze.
    Holds position, collision rect, and the engine lifecycle interface.
    """

    def __init__(self, x: float, y: float) -> None:
        self.x: float = x  # Pixel position in the screen
        self.y: float = y  # we don't use Rect because it can store only int
        self.rect: pygame.Rect = pygame.Rect(0, 0, 0, 0)
        # We keep the true pixel pos in float, then sync the rect at the end
        # of each frames with self.rect.center = (round(self.x), round(self.y))

    # To update what happen to the entity each frames
    @abstractmethod
    def update(self, dt: float) -> None:
        ...

    # To draw the entity on the surface for each moments/actions
    @abstractmethod
    def draw(self, surface: pygame.Surface,
             offset: tuple[int, int]) -> None:
        ...

    # To detect collisions with other entities
    # use pygame Axis-Aligned Bounding Box. We can change it to make
    # it more precise with like a circle based check for pac man char
    def collides_with(self, other_entity: "Entity") -> bool:
        return self.rect.colliderect(other_entity.rect)
