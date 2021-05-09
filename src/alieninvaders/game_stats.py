"""
This module stores the game Statistics.

When the game ends, the high-score is stored in a file and retrieved when
the game starts up again. Thus the highest score ever attained is tracked.
"""

from os import path, pardir

HIGH_SCORE_TXT = path.join(pardir, "resources/logs/high-scores.txt")


class GameStats:
    """Track statistics for Alien Invaders game."""

    def __init__(self, game):
        """Initialize statistics."""
        self.settings = game.settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        # Get score from file.
        self.high_score = self.file_score

    def reset_stats(self):
        """
        Set dynamic statistics for the game.

        Initialize statistics at the beginning of the game, or
        Reset the statistics as the game progresses.
        """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def write_highscore(self):
        """Write the high-score to file."""
        with open(HIGH_SCORE_TXT, "wt+") as f:
            try:
                score = int(f.read())
            # If the file contains a non-numeric value, set high-score to 0.
            except ValueError:
                score = 0
            finally:
                if self.high_score > score:
                    f.write(str(self.high_score))

    @property
    def file_score(self) -> int:
        """Read the high-score from file."""
        with open(HIGH_SCORE_TXT) as f:
            try:
                score = int(f.read())
            # If the file contains a non-numeric value, set high-score to 0.
            except ValueError:
                return 0
            else:
                return score
