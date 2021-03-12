""" Main Game Module"""

import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game asserts and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode(
            (Settings.SCREEN_WIDTH, Settings.SCREEN_WIDTH))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Start main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(Settings.BG_COLOR)

            # Make the most recent screen visible.
            pygame.display.flip()

    if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()