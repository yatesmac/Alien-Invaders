"""
This module handles the information contained in the scored-board.

The score-board appears at the top of the game screen, showing:
    the number of lives left,
    the high-score,
    the current game score, and
    the current game level.
 """

from os import path, pardir

import pygame as pg
from pygame.sprite import Group

import color
from ship import Ship

DEFAULT_PATH = path.join(pardir, "resources/")
SHIP_IMG = DEFAULT_PATH + "images/ship.bmp"
FONT = DEFAULT_PATH + "fonts/nunito.ttf"


class DisplayShip(Ship):
    """
    A class representing smaller ships that represent the player's lives.
    """

    def __init__(self, game):
        super().__init__(game)

    @property
    def image(self) -> pg.Surface:
        image = pg.image.load(SHIP_IMG).convert()
        image = pg.transform.scale(image, (26, 30))
        image.set_colorkey(color.WHITE)
        return image


class ScoreBoard:
    """A class to report scoring information."""

    def __init__(self, game):
        """Initialize score-keeping attributes."""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = game.stats

        # Font settings for scoring information.
        self.text_color = color.BLACK
        self.font = pg.font.Font(FONT, 16)

        self.prep_images()

    def prep_images(self):
        """Prepare the initial score images."""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def _render_image(self, value_string: str, value: int) -> pg.Surface:
        """Turn game value into rendered image."""
        # Round the score to a multiple of ten, without affecting level.
        rounded_value: int = round(value, -1) if value > 500 else value

        value_str = f"{value_string}: {rounded_value:,}"
        return self.font.render(value_str, True, self.text_color, color.BG_GRAY)

    def prep_score(self):
        """Position the rendered score on the game screen."""
        self.score_image = self._render_image("Score", self.stats.score)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 25
        self.score_rect.top = 5

    def prep_high_score(self):
        """Position the rendered high score on the game screen."""
        self.high_score_image = self._render_image("High Score", self.stats.high_score)

        # Display the score at rhe top right of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 5

    def prep_level(self):
        """Position the rendered value on the game screen."""
        self.level_image = self._render_image("Level", self.stats.level)

        # Display the score at the top right of the screen.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 25
        self.level_rect.top = self.score_rect.bottom + 5

    def prep_ships(self):
        """Show how many lives are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = DisplayShip(self.game)
            ship.rect.x = 5 + ship_number * ship.rect.width
            ship.rect.y = 5
            self.ships.add(ship)

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw scores, level and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
