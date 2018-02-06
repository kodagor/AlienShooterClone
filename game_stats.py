class GameStats:
    """ Monitoring statistics in game"""

    def __init__(self, ai_settings):
        """"Init statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # best score
        self.high_score = 0

    def reset_stats(self):
        """init statistics, which can change while in game"""
        self.ships_left = self.ai_settings.ships_limit
        self.score = 0
        self.level = 1
        # running game in inactive state
        self.game_active = False

