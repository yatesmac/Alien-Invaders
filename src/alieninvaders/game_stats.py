from os import path, pardir

HIGH_SCORE_TXT = path.join(pardir, 'resources/logs/high-scores.txt')


class GameStats:
    """TRack statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        # Get score from file.
        self.high_score = self.file_score

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def write_highscore(self):
        """Write the high-score to file."""
        with open(HIGH_SCORE_TXT, 'wt+') as f:
            try:
                score = int(f.read())
            # If the file contains a non-numeric value, set high-score to 0.
            except ValueError:
                score = 0
            finally:
                if self.high_score > score:
                    f.write(str(self.high_score))

    @property
    def file_score(self):
        """Read the high-score from file."""
        with open(HIGH_SCORE_TXT) as f:
            try:
                score = int(f.read())
            # If the file contains a non-numeric value, set high-score to 0.
            except ValueError:
                return 0
            else:
                return score


