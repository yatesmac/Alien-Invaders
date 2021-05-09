"""This module stores the Settings for the game."""


class Settings:
    """A class to store all the static and dynamic settings for Alien Invaders game."""

    # Constant game settings are stored as class attributes.

    # Screen
    screen_width = 900
    screen_height = 600
    # Ship
    ship_limit = 3
    # Bullet
    bullets_limit = 3
    # Alien
    fleet_drop_speed = 5
    # How quickly the game speeds up.
    speedup_scale = 1.1
    # How quickly the alien point values increase.
    score_scale = 1.5

    def __init__(self):
        """Initialize the game's dynamic settings."""
        self.initialize_dynamic_settings()

        # fleet_direction of 1 represents right; -1, left.
        self.fleet_direction = 1
        # Game volume, 1 is sounds on and -1 is sounds off.
        self.sound_playing = -1

    def initialize_dynamic_settings(self):
        """
        Set dynamic settings for the game.

        Initialize settings at the beginning of the game, or
        Reset the ship's dynamic settings as the game progresses.
        """
        self.ship_speed = 2.5
        self.bullet_speed = 7.5
        self.alien_speed = 1.0
        # Scoring
        self.alien_points = 50

    def increase_level(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


