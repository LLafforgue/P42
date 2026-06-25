from __future__ import annotations
from abc import abstractmethod
import pygame

from .entities import Entity


# Update and draw of entities will be called into the GameView
# screen, in a loop like the main game loop
class Collectible(Entity):
    ...
