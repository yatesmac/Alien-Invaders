"""Main Game Module"""

from os import path, pardir
import sys
from time import sleep

import pygame as pg
from pygame.mixer import Sound
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

from alien_fleet import Fleet
from bullet import Bullet
from button import Button
from game_stats import GameStats
from scoreboard import ScoreBoard
from settings import Settings
from ship import Ship

SHOOT_WAV = path.join(pardir, 'resources/sounds/shoot.wav')
SHIP_HIT_WAV = path.join(pardir, 'resources/sounds/ship_hit.wav')
SHOT_ALIEN_WAV = path.join(pardir, 'resources/sounds/alien_shot.wav')


def main():
    """Create the entry point for the game."""
    game = AlienInvasion()

    while True:
        game.check_events()

        if game.stats.game_active:
            game.ship.update()
            game.update_bullets()
            game.update_aliens()

        game.update_screen()


class AlienInvasion:
    """Overall class to manage game asserts and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        self._init_pygame()
        self.settings = Settings()
        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.clock = pg.time.Clock()
        self.stats = GameStats(self)
        self.score_board = ScoreBoard(self)
        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()

        self.fleet = Fleet(self)
        self.aliens = self.fleet.aliens
        self.play_button = Button(self, 'Click here or press Enter to play')

        # Sounds
        self.shooting_sound = Sound(SHOOT_WAV)
        self.ship_hit_sound = Sound(SHIP_HIT_WAV)
        self.alien_shot_sound = Sound(SHOT_ALIEN_WAV)
        for _sound in (
            self.shooting_sound,
            self.ship_hit_sound,
            self.alien_shot_sound
        ):
            _sound.set_volume(0.2)

    @staticmethod
    def _init_pygame():
        """Initialize pygame and caption the game window."""
        pg.init()
        pg.display.set_caption('Alien Invaders')

    def check_events(self):
        """Respond to key presses and mouse events."""
        for event in pg.event.get():
            if self._quit_game(event):
                self.stats.write_highscore()
                sys.exit()

            if self._start_game(event) and not self.stats.game_active:
                # Reset the game settings
                self.settings.initialize_dynamic_settings()
                self._setup_new_game()

            if event.type == KEYDOWN:
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
        self.score_board.prep_ships()

        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship
        self.fleet.create_fleet()
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
            self.shooting_sound.play()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collision."""
        # Remove any bullets and aliens that have collided.
        collisions = pg.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.alien_shot_sound.play()
                self.score_board.prep_score()
            self.score_board.check_high_score()

        if not self.aliens:
            # Destroy existing bullets, create new fleet, increase game speed.
            self.bullets.empty()
            self.fleet.create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.score_board.prep_level()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left < 1:  # no more lives left
            self.stats.game_active = False
            pg.mouse.set_visible(True)

        self.ship_hit_sound.play()
        sleep(0.5)

        # Decrement ships left, and update score-board
        self.stats.ships_left -= 1
        self.score_board.prep_ships()

        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship
        self.fleet.create_fleet()
        self.ship.center_ship()

        # Pause
        sleep(1.0)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this as the same as if the ship hot hit.
                self._ship_hit()
                break

    def update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def update_aliens(self):
        """Update the position of all aliens in the fleet."""
        self.fleet.check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pg.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom og the screen.
        self._check_aliens_bottom()

    def update_screen(self):
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
        self.clock.tick(60)


if __name__ == '__main__':
    main()
