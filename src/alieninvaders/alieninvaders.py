"""
The main game module.

Contains:
    the main function, which is the entry point for the game, and
    the AlienInvaders class which handles the game logic.
In order for the AlienInvaders attributes and methods to be accessible
across all game modules, an instance of the class is passed to the initializers
of some classes as the argument "game."
"""

from os import pardir, path
import sys
from time import sleep

import pygame as pg
from pygame.mixer import Sound
from pygame.locals import (
    K_ESCAPE,
    K_LEFT,
    K_RETURN,
    K_RIGHT,
    K_SPACE,
    KEYDOWN,
    KEYUP,
    MOUSEBUTTONDOWN,
    QUIT,
    K_m,
)

from alien_fleet import Fleet
from bullet import Bullet
from button import Button, Tag
from game_stats import GameStats
from scoreboard import ScoreBoard
from settings import Settings
from ship import Ship

DEFAULT_PATH = path.join(pardir, "resources/")
BACKGROUND_IMG = DEFAULT_PATH + "images/back.bmp"
SHOOT_WAV = DEFAULT_PATH + "sounds/shoot.wav"
SHIP_HIT_WAV = DEFAULT_PATH + "sounds/ship_hit.wav"
SHOT_ALIEN_WAV = DEFAULT_PATH + "sounds/alien_shot.wav"


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
        self.ship = Ship(self)
        self.stats = GameStats(self)
        self.score_board = ScoreBoard(self)
        self.fleet = Fleet(self)

        self.aliens = self.fleet.aliens
        self.bullets = pg.sprite.Group()
        self.clock = pg.time.Clock()

        # Button and Tag
        self.play_button = Button(self)
        self.info_tag = Tag(self)

        # Sounds
        self.shooting_sound = Sound(SHOOT_WAV)
        self.ship_hit_sound = Sound(SHIP_HIT_WAV)
        self.alien_shot_sound = Sound(SHOT_ALIEN_WAV)
        self._update_sounds()

    @staticmethod
    def _init_pygame():
        """Initialize pygame and caption the game window."""
        pg.init()
        pg.display.set_caption("Alien Invaders")

    def check_events(self):
        """Respond to key presses and mouse events."""
        for event in pg.event.get():
            if self._quit_game(event):
                # Write high-score to file then Exit.
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
    def _quit_game(event: pg.event.Event) -> bool:
        """Check if the user wants to exit the game."""
        return event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)

    def _start_game(self, event: pg.event.Event) -> bool:
        """Start a new game when the clicks Play or hits Enter"""
        # The player clicks Play.
        if event.type == MOUSEBUTTONDOWN:
            return self.play_button.rect.collidepoint(pg.mouse.get_pos())
        # The player presses enter.
        return event.type == KEYDOWN and event.key == K_RETURN

    def _setup_new_game(self):
        """Reset the game statistics and create a new board."""
        self.stats.reset_stats()
        self.stats.game_active = True
        self.score_board.prep_images()
        self._reset_sprites()

        # Hide the mouse cursor.
        pg.mouse.set_visible(False)

    def _reset_sprites(self):
        """Remove old bullets and aliens, create a new ship and alien fleet."""
        self.aliens.empty()
        self.bullets.empty()
        self.fleet.create_fleet()
        self.ship.center_ship()

    def _check_keydown_events(self, event: pg.event.Event):
        """Respond to key presses."""
        if event.key == K_RIGHT:
            self.ship.moving_right = True
        elif event.key == K_LEFT:
            self.ship.moving_left = True
        elif event.key == K_SPACE:
            self._fire_bullet()
        elif event.key == K_m:
            self._update_sounds()

    def _check_keyup_events(self, event: pg.event.Event):
        """Respond to key releases."""
        if event.key == K_RIGHT:
            self.ship.moving_right = False
        elif event.key == K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.shooting_sound.play()

    def _alien_bullet_collision(self):
        """Respond to bullet-alien collision."""
        # Remove any bullets and aliens that have collided.
        collisions = pg.sprite.groupcollide(self.bullets, self.aliens, True, True)

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
            self.settings.increase_level()

            # Increase level.
            self.stats.level += 1
            self.score_board.prep_level()

    def _alien_ship_collision(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left < 1:  # no more lives left
            self.stats.game_active = False
            pg.mouse.set_visible(True)

        self.ship_hit_sound.play()
        sleep(0.5)

        # Decrement ships left, and update score-board
        self.stats.ships_left -= 1
        self.score_board.prep_ships()

        self._reset_sprites()
        sleep(1.0)

    def _alien_ground_collision(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this as the same as if the ship hot hit.
                self._alien_ship_collision()
                break

    def _update_sounds(self):
        """Plays sounds if play = 1, stops sounds if play = -1"""
        # Defaults to 1, sounds enabled.
        self.settings.sound_playing *= -1
        for _sound in (
            self.shooting_sound,
            self.ship_hit_sound,
            self.alien_shot_sound,
        ):
            if self.settings.sound_playing == 1:
                _sound.set_volume(0.2)
            elif self.settings.sound_playing == -1:
                _sound.set_volume(0)

    def update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._alien_bullet_collision()

    def update_aliens(self):
        """Update the position of all aliens in the fleet."""
        self.fleet.check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pg.sprite.spritecollideany(self.ship, self.aliens):
            self._alien_ship_collision()

        # Look for aliens hitting the bottom og the screen.
        self._alien_ground_collision()

    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        background = pg.image.load(BACKGROUND_IMG).convert()
        bg_image = pg.transform.scale(
            background, (self.settings.screen_width, self.settings.screen_height)
        )
        self.screen.blit(bg_image, (0, 0))
        self.ship.draw_ship()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the score information
        self.score_board.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            # Button and Tag
            self.info_tag.prep_msg(
                "Press Esc to exit. Press M to (un)mute game sounds."
            )
            self.info_tag.draw_button()
            self.play_button.prep_msg("Click here or press Enter to play.")
            self.play_button.draw_button()

        pg.display.flip()
        self.clock.tick(60)



if __name__ == "__main__":
    main()
