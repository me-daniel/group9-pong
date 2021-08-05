"""
This Module contains the CPU class and its functions.

Classes: CPU
Functions: move(self)
"""

import pygame
import os
import random


class CPU:
    """
    A class to represent the CPU and handle its movements.

    Attributes
    ----------
    player.image : pygame.image
        initializes the image
    player_rect : pygame.rect
        initializes the player rectangle
    score : int
        current score of the CPU
    ball : ball
        initializes the ball

    Methods
    -------
    move:
        Moves the CPU
    """

    def __init__(self, ball):
        """Initialize class variables."""
        # Load the player image for the CPU and position its rectangle.
        self.player_image = pygame.image.load(os.path.join(
            'graphics', 'pong_player_1.png')).convert_alpha()
        self.player_rect = self.player_image.get_rect(topright=(1180, 200))
        self.score = 0
        self.ball = ball

    def move(self):
        """Moves the CPU.

        Keyword arguments:
        self -- applies on itself
        """

        # If the ball moves towards the CPU and crosses the vertival midline of screen move
        if self.ball.x_vel > 0 and self.ball.ball_rect.center[0] > 640:
            # If the CPUs rectangle does not cross the screen border,
            # move it in the direction of the ball on the y axis with a probability of 0.5 every frame.
            if self.ball.ball_rect.center[1] > self.player_rect.center[1] and self.player_rect.bottom < 720:
                self.player_rect.y += 10*random.randint(0, 1)
            elif self.ball.ball_rect.center[1] < self.player_rect.center[1] and self.player_rect.top > 0:
                self.player_rect.y -= 10*random.randint(0, 1)
