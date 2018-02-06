import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """initialization the ship and his starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load picture and his rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # every new ship appears in the bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 2

        # ship middle point as a floating number
        self.center = float(self.rect.centerx)

        # options pointing ship movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update ship position according to option pointing his movement"""

        # update value of the ship's middle point, not his rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect object according to value of self.center
        self.rect.centerx = self.center

    def blitme(self):
        """displaying ship on his position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """place ship at the center bottom screen edge"""
        self.center = self.screen_rect.centerx
