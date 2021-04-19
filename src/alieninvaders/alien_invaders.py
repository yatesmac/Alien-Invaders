"""Main Game Module"""

import sys
from time import sleep

import pygame as pg
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_RETURN,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
    MOUSEBUTTONDOWN,
)

from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
from scoreboard import ScoreBoard
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game asserts and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        self._init_pygame()
        self.settings = Settings()
        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.stats = GameStats(self)
        self.score_board = ScoreBoard(self)
        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()
        self.aliens = pg.sprite.Group()
        self._create_fleet()

        # Make a Play button
        self.play_button = Button(self, 'Click here or press Enter to play')

    def run_game(self):
        """Start main loop for the game."""
        while True:
            self._check_events()

            # First check if the user still has lives.
            if self.stats.game_active:
                self._update_ship()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    @staticmethod
    def _init_pygame():
        """Initialize pygame."""
        pg.init()
        pg.display.set_caption('Alien Invaders')

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pg.event.get():
            if self._quit_game(event):
                sys.exit()

            if self._start_game(event) and not self.stats.game_active:
                # Reset the game settings
                self.settings.initialize_dynamic_settings()
                self._setup_new_game()
            elif event.type == KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == KEYUP:
                self._check_keyup_events(event)

    @staticmethod
    def _quit_game(event):
        """Check if the user wants to exit the game."""
        return event.type == QUIT or (
                event.type == KEYDOWN and
                event.key == K_ESCAPE
        )

    def _start_game(self, event):
        """Start a new game when the clicks Play or hits Enter"""
        # The player clicks Play.
        if event.type == MOUSEBUTTONDOWN:
            return self.play_button.rect.collidepoint(
                pg.mouse.get_pos()
            )
        # The player presses enter.
        else:
            return event.type == KEYDOWN and event.key == K_RETURN

    def _setup_new_game(self):
        """Reset the game statistics and create a new board."""
        self.stats.reset_stats()
        self.stats.game_active = True
        self.score_board.prep_score()
        self.score_board.prep_level()

        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor.
        pg.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == K_RIGHT:
            self.ship.moving_right = True
        elif event.key == K_LEFT:
            self.ship.moving_left = True
        elif event.key == K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == K_RIGHT:
            self.ship.moving_right = False
        elif event.key == K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collision."""
        # Remove any bullets and aliens that have collided.
        collisions = pg.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.score_board.prep_score()
            self.score_board.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.score_board.prep_level()

    def _update_ship(self):
        """Update the ship's position on the board."""
        self.ship.update()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left < 1:  # no more lives left
            self.stats.game_active = False
            pg.mouse.set_visible(True)

        # Decrement ships left
        self.stats.ships_left -= 1

        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()
        self.settings.increase_speed()

        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # Pause
        sleep(1.0)

    def _update_aliens(self):
        """Update the position of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pg.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom og the screen.
        self._check_aliens_bottom()

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 3 / 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (3/2 * alien_width)
        number_of_aliens_x = int(available_space_x / (3/2 * alien_width))

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (
                self.settings.screen_height
                - (3 * alien_height)
                - (3 * ship_height)
        )
        number_rows = available_space_y // (2 * alien_height)

        # Create fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_of_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this as the same as if the ship hot hit.
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.draw_ship()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the score information
        self.score_board.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pg.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()