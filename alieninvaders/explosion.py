"""This module handles the creation of an Explosion instance."""

from os import pardir, path

import pygame as pg
from pygame.sprite import Sprite

import color

# Path template for the nine explosion images.
IMG = path.join(pardir, "resources/images/explosions/explosion0{}.jpg")


class Explosion(Sprite):
    """A class to simulate an explosion in the event of a collision."""

    def __init__(self, center):
        """Create an explosion object in the rect center of the alien that was shot."""
        super().__init__()
        self.frame = 0  # Corresponds to each image in the simulation.
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 75
        # The list of images that simulate the explosion.
        self.explosion_sim = []
        self._prep_images()
        self.image = self.explosion_sim[0]  # Corresponds to images in the simulation.
        self.rect = self.image.get_rect()
        self.rect.center = center

    def _prep_images(self):
        """Load each explosion image, remove background and add to explosion list."""
        for i in range(9):  # There are nine images.
            image = pg.image.load(IMG.format(i)).convert()
            image = pg.transform.scale(image, (55, 55))
            image.set_colorkey(color.BLACK)
            self.explosion_sim.append(image)

    def update(self):
        """Cycle through the explosion images."""
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            # Remove the sprite when it has cycled through all images.
            if self.frame == len(self.explosion_sim):
                self.kill()
            else:
                # Display the current image at the mid-point of where the alien was.
                center = self.rect.center
                self.image = self.explosion_sim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
