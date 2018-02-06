class Settings():
    """class for game settings"""

    def __init__(self):
        """static settings"""
        # screen settings
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (0, 0, 0)

        # ship settings
        self.ships_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 230, 230, 230
        self.bullets_allowed = 3

        # alien settings
        self.fleet_drop_speed = 10

        # stars settings
        # self.star_speed_factor = 1

        # easy change game speed
        self.speedup_scale = 1.1
        # change points value
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """init setting, which are changing during game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet direction = -1 => left; +1 => right
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """change speed settings and points gained"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
