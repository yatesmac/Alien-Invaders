import os

import pygame as pg
from pygame.sprite import Sprite

ALIEN_PATH = os.path.join(os.pardir, 'resources/images/alien.bmp')


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set it's starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the alien image and set its rect attribute.
        self.image = pg.image.load(ALIEN_PATH)
        # Remove background from ship image
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens' exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return (
                self.rect.right >= screen_rect.right or
                self.rect.left <= 0
        )

    def update(self):
        """Move the alien to the right or left."""
        self.x += (
            self.settings.alien_speed * self.settings.fleet_direction
        )
        self.rect.x = self.x