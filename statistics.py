# Environmental modules
from decimal import Decimal


class BasicStatistics():

    def __init__(self, minutes_played, field_goals, field_goal_attempts, field_goal_percentage, 
                 two_point_field_goals, two_point_field_goal_attempts, two_point_field_goal_percentage,
                 three_point_field_goals, three_point_field_goal_attempts, three_point_field_goal_percentage, 
                 free_throws, free_throw_attempts, free_throw_percentage, offensive_rebounds, 
                 defensive_rebounds, total_rebounds, assists, steals, blocks, turnovers,
                 personal_fouls, points):

        self.minutes_played = minutes_played
        self.field_goals = field_goals
        self.field_goal_attempts = field_goal_attempts
        self.field_goal_percentage = field_goal_percentage
        self.two_point_field_goals = two_point_field_goals
        self.two_point_field_goal_attempts = two_point_field_goal_attempts
        self.two_point_field_goal_percentage = two_point_field_goal_percentage
        self.three_point_field_goals = three_point_field_goals
        self.three_point_field_goal_attempts = three_point_field_goal_attempts
        self.three_point_field_goal_percentage = three_point_field_goal_percentage
        self.free_throws = free_throws
        self.free_throw_attempts = free_throw_attempts
        self.free_throw_percentage = free_throw_percentage
        self.offensive_rebounds = offensive_rebounds
        self.defensive_rebounds = defensive_rebounds
        self.total_rebounds = total_rebounds
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers
        self.personal_fouls = personal_fouls
        self.points = points


class AdvancedStatistics():

    def __init__(self, true_shooting_percentage, effective_field_goal_percentage,
                 three_point_attempt_rate, free_throw_attempt_rate, offensive_rebound_percentage,
                 defensive_rebound_percentage, total_rebound_percentage, assist_percentage,
                 steal_percentage, block_percentage, turnover_percentage, usage_percentage,
                 offensive_rating, defensive_rating):

        self.true_shooting_percentage = true_shooting_percentage
        self.effective_field_goal_percentage = effective_field_goal_percentage
        self.three_point_attempt_rate = three_point_attempt_rate
        self.free_throw_attempt_rate = free_throw_attempt_rate
        self.offensive_rebound_percentage = offensive_rebound_percentage
        self.defensive_rebound_percentage = defensive_rebound_percentage
        self.total_rebound_percentage = total_rebound_percentage
        self.assist_percentage = assist_percentage
        self.steal_percentage = steal_percentage
        self.block_percentage = block_percentage
        self.turnover_percentage = turnover_percentage
        self.usage_percentage = usage_percentage
        self.offensive_rating = offensive_rating
        self.defensive_rating = defensive_rating


class Statistics(BasicStatistics, AdvancedStatistics):
    pass