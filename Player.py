"""
This Module contains the Player class and its functions.

Classes: Player
Functions: move(self)
"""

import pygame
import os


class Player:
    """
    A class to represent a Player.

    Attributes
    ----------
    player_image : pygame.image
        initializes the image
    player_num : int
        tell if its player 1 or 2
    score : int
        keeps track of the score

    Methods
    -------
    move:
        Moves the player
    """

    def __init__(self, player_num):
        """Initialize class variables.

        Keyword arguments:
        self -- applies on itself
        player_num -- determines if its player 1 or 2
        """

        # Load the player image and position of the player rectangle according to the player number.
        self.player_num = player_num

        if player_num == 1:
            self.player_image = pygame.image.load(os.path.join(
                'graphics', 'pong_player_1.png')).convert_alpha()
            self.player_rect = self.player_image.get_rect(topleft=(100, 200))

        if player_num == 2:
            self.player_image = pygame.image.load(os.path.join(
                'graphics', 'pong_player_2.png')).convert_alpha()
            self.player_rect = self.player_image.get_rect(topright=(1180, 200))

        self.score = 0

    def move(self):
        """Moves the player by reading the keys.

        Keyword arguments:
        self -- applies on itself
        """

        # Read the keys.
        keys = pygame.key.get_pressed()

        # Move player 1 when the w or s key is pressed and the player is still within the limits of the screen.
        if self.player_num == 1:
            if keys[pygame.K_s] and self.player_rect.bottom < 720:
                self.player_rect.y += 10

            if keys[pygame.K_w] and self.player_rect.top > 0:
                self.player_rect.y -= 10

        # Move player 2 when the down or up key is pressed and the player is still within the limits of the screen.
        else:
            if keys[pygame.K_DOWN] and self.player_rect.bottom < 720:
                self.player_rect.y += 10

            if keys[pygame.K_UP] and self.player_rect.top > 0:
                self.player_rect.y -= 10
