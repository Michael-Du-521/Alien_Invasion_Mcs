import pygame


class Ship:
    """Control ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        """Load the ship's image ,and get its rectangular outside """
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        """For every ship, locate it on the bottom of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        """Indicater for moving"""
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blit(self):
        """Draw the ship at place specified"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        """update the ship.rect.x based on self.x"""
        self.rect.x = self.x
        if self.moving_up and self.rect.top > self.screen_rect.top:  # depend on the coordinate
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y
