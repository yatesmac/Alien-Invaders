import pygame.font

class ScoreBoard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize score-keeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 24)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def _render_image(self, value_string, value):
        """Turn game value into rendered image."""
        rounded_value = round(value, -1) if value > 500 else value
        value_str = f'{value_string}: {rounded_value:,}'
        return self.font.render(
            value_str, True, self.text_color, self.settings.bg_color
        )

    def prep_score(self):
        """Position the rendered score on the game screen."""
        self.score_image = self._render_image('Score', self.stats.score)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 25
        self.score_rect.top = self.screen_rect.top

    def prep_high_score(self):
        """Position the rendered high score on the game screen."""
        self.high_score_image = self._render_image(
            'High Score', self.stats.high_score
        )

        # Display the score at rhe top right of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """Position the rendered value on the game screen."""
        self.level_image = self._render_image('Level', self.stats.level)

        # Display the score at the top right of the screen.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 25
        self.level_rect.top = self.score_rect.bottom + 5

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw scores and level to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)