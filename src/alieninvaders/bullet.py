import os

import pygame as pg
from pygame.sprite import Sprite

BULLET_PATH = os.path.join(os.pardir, 'resources/images/bullet.bmp')


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the bullet image and get its rect.
        self.image = pg.image.load(BULLET_PATH).convert()
        # Remove background from ship image
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        # self.color = self.settings.bullet_color
        # Create a bullet rect at (0, 0) and then set correct position
        # self.rect = pg.Rect(
        #    0, 0, self.settings.bullet_width, self.settings.bullet_height
        # )
        self.rect.midtop = ai_game.ship.rect.midtop

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
        # pg.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)