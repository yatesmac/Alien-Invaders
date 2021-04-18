class Settings:
    """A class to store all settings for Alien Invaders"""

    # Constant game settings
    # Screen
    screen_width = 900
    screen_height = 600
    bg_color = (230, 230, 230)

    # Ship
    ship_limit = 3

    # Bullet
    bullets_allowed = 3

    # Alien
    fleet_drop_speed = 5

    # How quickly the game speeds up.
    speedup_scale = 1.2

    def __init__(self):
        """Initialize the game's dynamic settings."""
        self.initialize_dynamic_settings()

        # fleet_direction of 1 represents right; -1, left.
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        """Reset the ship's dynamic settings."""
        self.ship_speed = 0.75
        self.bullet_speed = 0.75
        self.alien_speed = 0.1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale




