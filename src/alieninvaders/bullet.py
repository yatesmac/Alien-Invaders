"""This module handles the creation of a single Bullet instance."""

from os import path, pardir

import pygame as pg
from pygame.sprite import Sprite

import color

BULLET_IMG = path.join(pardir, 'resources/images/bullet.bmp')


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load the bullet image and remove background.
        self.image = pg.image.load(BULLET_IMG).convert()
        self.image.set_colorkey(color.WHITE)

        self.rect = self.image.get_rect()
        # Create a bullet rect at the top of the ship.
        self.rect.midtop = game.ship.rect.midtop
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
