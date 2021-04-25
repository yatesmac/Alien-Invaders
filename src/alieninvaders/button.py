from os import path, pardir

import pygame as pg

FONT = path.join(pardir, 'resources/fonts/nunito.ttf')


class Button:
    """A class to create a generic button."""

    # Set the static properties of the button.
    width, height = 350, 45
    button_color = (100, 100, 100)
    text_color = (255, 255, 255)

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.font = pg.font.Font(FONT, 14)

        # Build the button's rect object and center it.
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)