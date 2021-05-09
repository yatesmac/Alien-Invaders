"""This module handles the creation of a single Alien Ship instance."""

from os import path, pardir

import pygame as pg
from pygame.sprite import Sprite

import color

ALIEN_IMG = path.join(pardir, 'resources/images/alien.bmp')


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, game):
        """Initialize the alien and set it's starting position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load the alien image and remove background.
        self.image = pg.image.load(ALIEN_IMG).convert()
        self.image.set_colorkey(color.WHITE)

        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the aliens' exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self) -> bool:
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return (
                self.rect.right >= screen_rect.right or
                self.rect.left <= 0
        )

    def update(self):
        """Move the alien to the right or left."""
        self.x += (
            self.settings.alien_speed
            * self.settings.fleet_direction
        )
        self.rect.x = self.x