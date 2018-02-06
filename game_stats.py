class GameStats:
    """ Monitoring statistics in game"""

    def __init__(self, ai_settings):
        """"Init statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """init statistics, wich can change while in game"""
        self.ships_left = self.ai_settings.ships_limit
        # running game in inactive state
        self.game_active = False

