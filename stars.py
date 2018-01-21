import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """class for star"""

    def __init__(self, ai_settings, screen):
        """Init a star and define it's pos"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load star image
        self.image = pygame.image.load('images/start.bmp')
        self.rect = self.image.get_rect()

        # display a single star
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # exact star pos
        self.x = float(self.rect.x)

    def check_edge(self):
        """check if bottom edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True

    def blitme(self):
        """displaying a star in pos"""
        self.screen.blit(self.image, self.rect)

