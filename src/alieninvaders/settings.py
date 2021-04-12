class Settings:
    """A class to store all settings for Alien Invaders"""

    # Constant game settings
    # Screen settings
    screen_width = 1200
    screen_height = 800
    bg_color = (230, 230, 230)

    # Bullet settings
    bullet_speed = 1.0
    bullet_width = 3
    bullet_height = 70
    bullet_color = (0, 255, 55)
    bullets_allowed = 5

    def __init__(self):
        """Initialize the game's settings."""
        # Ship settings
        self.ship_speed = 1.5


