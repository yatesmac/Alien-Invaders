class Settings:
    """A class to store all settings for Alien Invaders"""

    # Constant game settings
    # Screen settings
    screen_width = 900
    screen_height = 600
    bg_color = (230, 230, 230)

    # Bullet settings
    bullet_speed = 1.0
    bullet_width = 3
    bullet_height = 45
    bullet_color = (255, 115, 0)
    bullets_allowed = 5

    # Alien settings
    alien_speed = 0.1
    fleet_drop_speed = 5

    def __init__(self):
        """Initialize the game's settings."""
        # Ship settings
        self.ship_speed = 0.75
        self.ship_limit = 3

        # Alien settings
        # fleet_direction of 1 represents right; -1, left.
        self.fleet_direction = 1


