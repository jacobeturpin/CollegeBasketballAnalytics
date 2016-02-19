class BasicStatistics():

    def __init__(self, minutes_played, field_goals, field_goal_attempts,
                 field_goal_percentage, two_point_field_goals,
                 two_point_field_goal_attempts,
                 two_point_field_goal_percentage,
                 three_point_field_goals,
                 three_point_field_goal_attempts,
                 three_point_field_goal_percentage, free_throws,
                 free_throw_attempts, free_throw_percentage,
                 offensive_rebounds, defensive_rebounds,
                 total_rebounds, assists, steals, blocks, turnovers,
                 personal_fouls, points):
        self.minutes_played = minutes_played
        self.field_goals = field_goals
        self.field_goal_attempts = field_goal_attempts


class AdvancedStatistics():

    def __init__(self, **kwargs):
        return super().__init__(**kwargs)