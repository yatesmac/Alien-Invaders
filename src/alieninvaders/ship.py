"""Module defining Player's Ship."""

from os import path, pardir

import pygame as pg
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        # self.ship_path = os.path.join(os.pardir, 'resources/images/ship.bmp')
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pg.image.load(self.ship_img).convert()
        # Remove background from ship image
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.center_ship()

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    @property
    def ship_img(self):
        return path.join(pardir, 'resources/images/ship.bmp')

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
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def draw_ship(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
