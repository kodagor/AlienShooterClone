import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Management bullets throwing by the ship"""

    def __init__(self, ai_setings, screen, ship):
        """Creating bullet object in present ship position"""

        super(Bullet, self).__init__()
        self.screen = screen

        # creating a rectangle in point 0,0 and defining his target location
        self.rect = pygame.Rect(0, 0, ai_setings.bullet_width, ai_setings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # position of bullet is defined by floating value
        self.y = float(self.rect.y)

        self.color = ai_setings.bullet_color
        self.speed_factor = ai_setings.bullet_speed_factor

    def update(self):
        """moving bullet on the screen"""
        # update bullet pos
        self.y -= self.speed_factor

        # update bullet rect pos
        self.rect.y = self.y

    def draw_bullet(self):
        """showing bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
