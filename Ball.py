"""
This Module contains the Ball class and its functions.

Classes: Ball
Functions: move(self)
"""

import pygame


class Ball:
    """
    A class to represent a ball.

    Attributes
    ----------
    ball_surf : pygame.Surface
        surface to display the ball
    ball_rect : pygame.Rect
        rectangle of the ball 
    x_vel : int
        velocity in x direction
    y_vel : int
        velocity in y direction

    Methods
    -------
    move:
        Moves the ball
    """

    def __init__(self):
        """Initialize class variables."""
        self.ball_surf = pygame.Surface((10, 10))
        self.ball_surf.fill("WHITE")
        self.ball_rect = self.ball_surf.get_rect(center=(640, 30))
        self.x_vel = 5
        self.y_vel = 5

    def move(self):
        """Moves the Ball.

        Keyword arguments:
        self -- applies on itself
        """

        # Turn the ball around if it touches the top or bottom screen border.
        if self.ball_rect.top <= 0:
            self.y_vel = -self.y_vel

        elif self.ball_rect.bottom > 720:
            self.y_vel = -self.y_vel

        # Move the ball.
        self.ball_rect.x += self.x_vel
        self.ball_rect.y += self.y_vel
