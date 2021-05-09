"""This module handles the creation of a Button or clear Tag instance."""

from os import path, pardir

import pygame as pg

import color

FONT = path.join(pardir, 'resources/fonts/nunito.ttf')


class Button:
    """A class to create a generic button."""

    # Set the static properties of the button.
    width, height = 450, 45
    button_color = color.BUTTON_GRAY
    text_color = color.WHITE

    def __init__(self, game):
        """Initialize Button attributes."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.font = pg.font.Font(FONT, 16)

        # Build the button's rect object and position it.
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = (self.screen_rect.centery - 25)

    def prep_msg(self, msg: str):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.centerx, self.rect.centery

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Tag(Button):
    """A class to create a generic clear tag. Extends Button."""

    def __init__(self, game):
        """Initialize Tag attributes that override Button attributes."""
        self.button_color = color.BG_GRAY
        self.text_color = color.BLACK
        self.screen_rect = game.screen.get_rect()

        self.rect = game.play_button.rect
        self.rect.centery = (self.screen_rect.centery + 25)

        super().__init__(game)



