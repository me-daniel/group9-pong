"""
This module contains the main Pong game loop. 

Functions: display_score()
"""

import pygame
from random import randint
from sys import exit
import os
import Player
import Ball
import CPU

pygame.init()
pygame.display.set_caption("Pong")

SCREEN = pygame.display.set_mode((1280, 720))
CLOCK = pygame.time.Clock()
FONT = pygame.font.Font(os.path.join('font', 'Pixeltype.ttf'), 50)

ball = Ball.Ball()
game_active = False

# Create the surface objects and rectangles for some text that is going to be displayed.
title_text_surf = FONT.render("PONG", True, "Orange")
options_text_surf = FONT.render(
    "Press 1 for Singleplayer or 2 for Multiplayer", True, "Yellow")
player1_win_text = FONT.render("Player 1 won!", True, "Skyblue")
player2_win_text = FONT.render("Player 2 won!", True, "Red")
controls_text_surf = FONT.render(
    "Use the W and S keys to control player 1", True, "Yellow")
controls_text_surf2 = FONT.render(
    "and the Up and Down keys to control player 2", True, "Yellow")

title_text_rect = title_text_surf.get_rect(center = (640, 100))
controls_text_rect = controls_text_surf.get_rect(center = (640, 620))
controls_text_rect2 = controls_text_surf2.get_rect(center = (640, 660))
win_text_rect = player1_win_text.get_rect(center=(640, 240))
options_text_rect = options_text_surf.get_rect(center=(640, 420))


def display_score():
    """Displays the score of each player on the screen."""
    score_p1_surface = FONT.render(str(player1.score), True, "Yellow")
    score_p1_rect = score_p1_surface.get_rect(midbottom=(320, 100))
    score_p2_surface = FONT.render(str(player2.score), True, "Yellow")
    score_p2_rect = score_p2_surface.get_rect(midbottom=(960, 100))

    SCREEN.blit(score_p1_surface, score_p1_rect)
    SCREEN.blit(score_p2_surface, score_p2_rect)


# This is the main game loop.
while True:
    # Check for the event that the player closes the game and close it.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active == False:
        # Display the option for Singleplayer and Multiplayer to the player.
        SCREEN.blit(title_text_surf, title_text_rect)
        SCREEN.blit(options_text_surf, options_text_rect)
        SCREEN.blit(controls_text_surf, controls_text_rect)
        SCREEN.blit(controls_text_surf2, controls_text_rect2)
        # Read the keys that are being pressed.
        # If the player presses 1 start the singeplayer mode and if the player presses 2 start the multiplayer mode.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            player1 = Player.Player(1)
            player2 = CPU.CPU(ball)
            game_active = True

        if keys[pygame.K_2]:
            player1 = Player.Player(1)
            player2 = Player.Player(2)

            game_active = True

    if game_active:
        # Move the player and ball objects.
        player1.move()
        player2.move()
        ball.move()

        # Create colliders for both players.
        collider_p1 = pygame.Rect(
            player1.player_rect.right, player1.player_rect.top, -1, player1.player_rect.height)
        collider_p2 = pygame.Rect(
            player2.player_rect.left, player2.player_rect.top, 1, player2.player_rect.height)

        # Check for collisions between the player colliders.  If they collide turn the ball around.
        if collider_p1.colliderect(ball.ball_rect):
            # Avoid multiple collisions between the ball and the player.
            ball.ball_rect.left = collider_p1.right
            ball.x_vel = -ball.x_vel

        if collider_p2.colliderect(ball.ball_rect):
            # Avoid multiple collisions between the ball and the player.
            ball.ball_rect.right = collider_p2.left
            ball.x_vel = -ball.x_vel

        # If the ball leaves the screen increase the score of the player that scored.
        if ball.ball_rect.left > 1280:
            player1.score += 1
            # Respawn the ball at a random y coordinate on the midline.
            ball.ball_rect.center = (640, randint(100, 620))
            ball.y_vel = abs(ball.y_vel)

        elif ball.ball_rect.right < 0:
            player2.score += 1
            ball.ball_rect.center = (640, randint(100, 620))
            ball.y_vel = abs(ball.y_vel)

        # Fill the background and draw the players, the ball and the score on the screen.
        SCREEN.fill((0, 0, 0))
        SCREEN.blit(player1.player_image, player1.player_rect)
        SCREEN.blit(player2.player_image, player2.player_rect)
        SCREEN.blit(ball.ball_surf, ball.ball_rect)
        display_score()

        # Check whether any player reached 10 points and show which player won.
        if player1.score == 10 or player2.score == 10:
            if player1.score > player2.score:
                SCREEN.blit(player1_win_text, win_text_rect)
            else:
                SCREEN.blit(player2_win_text, win_text_rect)
            game_active = False

    pygame.display.update()

    # Ensure the main game loop is maximally run 60 times per second.
    CLOCK.tick(60)
