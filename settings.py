class Settings():
    """class for game settings"""

    def __init__(self):
        """game setting init"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 768
        self.bg_color = (0, 0, 0)

        # ship settings
        self.ship_speed_factor = 1.5

        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 230, 230, 230
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 <- right; -1 <- left
        self.fleet_direction = 1

        # stars settings
        self.star_speed_factor = 1




