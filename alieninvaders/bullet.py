"""This module handles the creation of a single Bullet instance."""

from os import pardir, path

import pygame as pg
from pygame.sprite import Sprite

import color

BULLET_IMG = path.join(pardir, "resources/images/bullet.bmp")


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, game, x: int, top: int):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load the bullet image and remove background.
        self.image = pg.image.load(BULLET_IMG).convert()
        self.image.set_colorkey(color.WHITE)

        self.rect = self.image.get_rect()
        # Create a bullet rect at the top of the ship.
        self.rect.top = top
        self.rect.x = x

    def update(self):
        """Update the bullet position."""
        self.rect.y -= self.settings.bullet_speed
        # Get rid of bullets that have disappeared from the screen.
        if self.rect.bottom <= 0:
            self.kill()
