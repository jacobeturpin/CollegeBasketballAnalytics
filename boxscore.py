from statistics import *

class TeamBoxScore(BasicStatistics):

    def __init__(self, **kwargs):
        self.game_id = game_id
        self.team_id = team_id
        return super().__init__(**kwargs)


class PlayerBoxScore(BasicStatistics):

    def __init__(self, **kwargs):
        self.game_id = game_id
        self.player_id = player_id
        self.team_id = team_id
        return super().__init__(**kwargs)