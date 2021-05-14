"""This module handles the creation of the alien fleet."""

import pygame as pg

from alien import Alien


class Fleet:
    """A class to create a sprite group to store aliens in the alien fleet."""

    def __init__(self, game):
        """Initialize the game resources required for this class."""
        self.screen = game.screen
        self.settings = game.settings
        self.ship = game.ship

        # The sprite group where the aliens will be stored.
        self.aliens = pg.sprite.Group()

    def _create_alien(self, alien_number: int, row_number: int):
        """Create an alien and place it in the row."""
        # Create an alien.
        alien = Alien(self)
        alien_width, _ = alien.rect.size

        # Position each alien.
        alien.x = alien_width + 3 / 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 5 / 2 * alien.rect.height * row_number

        # Add the alien to the sprite group.
        self.aliens.add(alien)

    def create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Spacing between aliens is equal to one and a half (3/2) aliens width.
        available_space_x = self.settings.screen_width - (3 / 2 * alien_width)
        number_of_aliens_x = int(available_space_x / (3 / 2 * alien_width))

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - (3 * ship_height)
        )
        number_rows = available_space_y // (2 * alien_height)

        # Create fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_of_aliens_x):
                self._create_alien(alien_number, row_number)

    def check_fleet_edges(self):
        """Respond appropriately if any aliens have reached the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
