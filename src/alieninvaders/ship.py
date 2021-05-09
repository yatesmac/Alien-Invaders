"""This module handles the creation of a Ship instance."""

from os import path, pardir

import pygame as pg
from pygame.sprite import Sprite

import color

SHIP_IMG = path.join(pardir, 'resources/images/ship.bmp')


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.center_ship()

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    @property
    def image(self) -> pg.Surface:
        """Load the alien image and remove background."""
        image = pg.image.load(SHIP_IMG).convert()
        image.set_colorkey(color.WHITE)
        return image

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def draw_ship(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
