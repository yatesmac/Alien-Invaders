"""Module defining Player's Ship."""

import os

import pygame

# Ship Image Path.
SHIP_PATH = os.path.join(os.pardir, 'images/ship.bmp')


class Ship:
    """A class to manage the ship."""

    def __int__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.sceren.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load(SHIP_PATH)
        self.rect = self.image.get_rect()

        # Start eac new ship at the bottom center of the screen.
        self.rect.mid_bottom = self.screen_rect.mid_bottom

    def blit_me(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)





