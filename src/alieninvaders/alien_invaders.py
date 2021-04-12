""" Main Game Module"""

import sys

import pygame as pg
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT
)

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game asserts and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        self._init_pygame()
        self.screen = pg.display.set_mode(
            (Settings.SCREEN_WIDTH, Settings.SCREEN_WIDTH)
        )
        self.ship = Ship(self)

    def run_game(self):
        """Start main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    @staticmethod
    def _init_pygame():
        pg.init()
        pg.display.set_caption('Alien Invaders')

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pg.event.get():
            if event.type == QUIT or (
                event.type == KEYDOWN and
                event.key == K_ESCAPE
            ):
                sys.exit()

            elif event.type == KEYDOWN:
                if event.type == K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == K_LEFT:
                    self.ship.moving_left = True

            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
            self.screen.fill(Settings.BG_COLOR)
            self.ship.blitme()

            pg.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()