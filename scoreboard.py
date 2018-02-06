import pygame.sysfont
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """class for info about score"""

    def __init__(self, ai_settings, screen, stats):
        """init score attr"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # setting up a font
        self.text_color = (220, 220, 220)
        self.font = pygame.font.SysFont(None, 48)

        # prep img with score
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        """shows ships number, as lives"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * (ship.rect.width*1.15)
            ship.rect.y = 5
            self.ships.add(ship)

    def prep_high_score(self):
        """high score"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "High Score: "+"{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # draw highscore on the top center
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_score(self):
        """generate img from score"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "Score: "+"{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # displaying score in top right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        """create lvl num as image"""
        self.level_image = self.font.render("Lvl: "+str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        # level under score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """display score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # display ships
        self.ships.draw(self.screen)

