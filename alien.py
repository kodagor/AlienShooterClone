import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """class for alien in fleet"""

    def __init__(self, ai_settings, screen):
        """init alien and define his pos"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load alien image and define his rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # set pos in left top corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # keep alien's pos
        self.x = float(self.rect.x)

    def blitme(self):
        """display alien on his present pos"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """return True if alien is near the screen edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move alien right or left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

