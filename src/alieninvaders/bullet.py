from os import path, pardir

import pygame as pg
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the bullet image and get its rect.
        self.image = pg.image.load(self.bullet_img).convert()
        # Remove background from ship image
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        # Create a bullet rect at the top of our ship.
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    @property
    def bullet_img(self):
        return path.join(pardir, 'resources/images/bullet.bmp')

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


class Missile(Bullet):
    """A class to manage missiles fired by the aliens."""
    def __init__(self, ai_game):
        self.rect.midbottom = ai_game.alien.rect.midbottom

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        super().__init__(ai_game)

    @property
    def bullet_img(self):
        return path.join(pardir, 'resources/images/bullet.bmp')