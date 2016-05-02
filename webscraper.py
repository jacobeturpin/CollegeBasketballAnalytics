import requests, datetime, uuid
from bs4 import BeautifulSoup
from boxscore import *


class WebScraperManager():

    _url_root = 'http://sports-reference.com/cbb/'
    

    def __init__(self, **kwargs):
        self._last_scrape_date = None
        return super().__init__(**kwargs)


    def get_all_games_for_date(self, month, day, year):

        if datetime.date.today() < datetime.date(month=month, day=day, year=year):
            raise ValueError("Must use current or past date")

        url = str.format('{0}boxscores/index.cgi?month={1}&day={2}&year={3}',
                         self._url_root, month, day, year)
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        games = [link.get('href') for link in soup.find_all('a', text='Final')]
        return games


    def get_individual_game_data(self, game_link_address):
        r = requests.get(str.format('{0}{1}', _url_root, game_link_address))
        soup = BeautifulSoup(r.content, "html.parser")

        teams = self._get_individual_game_team_data(soup)
        team_stats = self._get_individual_teams_game_stats(soup, teams)
        player_stats = self._get_individual_players_game_stats(soup, teams)

        return {'teams': teams, 'teamStats': team_stats, 'playerStats': player_stats}


    def _get_individual_game_team_data(self, soup):
        
        staging = soup.find('th', text='Scoring').parent.parent
        content = staging.find_all('tr')[2:]

        # Inserting placeholder values where appropriate for now
        awayTeam = {
            'teamName': content[0].contents[1].text,
            'seasonYear': 2016,
            'gameDate': date(month=12, day=12, year=2012),
            'opponent': content[1].contents[1].text,
            'firstHalfScore': content[0].contents[3].text,
            'secondHalfScore': content[0].contents[5].text,
            'overtimeScore': None,
            'finalScore': content[0].contents[7].text,
            'finalResult': True if content[0].contents[7].text > content[1].contents[7].text else False
            }

        homeTeam = {
            'teamName': content[1].contents[1].text,
            'seasonYear': 2016,
            'gameDate': date(month=12, day=12, year=2012),
            'opponent': content[0].contents[1].text,
            'firstHalfScore': content[1].contents[3].text,
            'secondHalfScore': content[1].contents[5].text,
            'overtimeScore': None,
            'finalScore': content[1].contents[7].text,
            'finalResult': True if content[1].contents[7].text > content[0].contents[7].text else False
            }

        return [awayTeam, homeTeam]

    #Need to make tolerant of null statistical categories (even if not very likely at team level)
    def _get_individual_teams_game_stats(self, soup, teams):
        
        i, teamStats = 0, []
        staging = soup.find_all('th', text='Basic Box Score Stats')
        content = [x.parent.find_next('td', text='School Totals').parent.find_all('td')[1:] for x in staging]
        
        for team in teams:
            i += 1 

            minutes_played = int(content[i-1][0].text)
            field_goals = int(content[i-1][1].text)
            field_goal_attempts = int(content[i-1][2].text)
            field_goal_percentage = Decimal(content[i-1][3].text)
            two_point_field_goals = int(content[i-1][4].text)
            two_point_field_goal_attempts = int(content[i-1][5].text)
            two_point_field_goal_percentage = Decimal(content[i-1][6].text)
            three_point_field_goals = int(content[i-1][7].text)
            three_point_field_goal_attempts = int(content[i-1][8].text)
            three_point_field_goal_percentage = Decimal(content[i-1][9].text)
            free_throws = int(content[i-1][10].text)
            free_throw_attempts = int(content[i-1][11].text)
            free_throw_percentage = Decimal(content[i-1][12].text)
            offensive_rebounds = int(content[i-1][13].text)
            defensive_rebounds = int(content[i-1][14].text)
            total_rebounds = int(content[i-1][15].text)
            assists = int(content[i-1][16].text)
            steals = int(content[i-1][17].text)
            blocks = int(content[i-1][18].text)
            turnovers = int(content[i-1][19].text)
            personal_fouls = int(content[i-1][20].text)
            points = int(content[i-1][21].text)

            teamStats.append(TeamBoxScore(minutes_played, field_goals, field_goal_attempts, field_goal_percentage, two_point_field_goals, 
                                          two_point_field_goal_attempts, two_point_field_goal_percentage, three_point_field_goals, 
                                          three_point_field_goal_attempts, three_point_field_goal_percentage, free_throws, free_throw_attempts, 
                                          free_throw_percentage, offensive_rebounds, defensive_rebounds, total_rebounds, assists, 
                                          steals, blocks, turnovers, personal_fouls, points))

        return teamStats


    # Need to make tolerant of null statistical categories
    def _get_individual_players_game_stats(self, soup):
        
        i, playerStats = 0, []

        for team in soup.find_all('th', text='Basic Box Score Stats'):
        
            # Use modulo to test for home/away status
            i += 1

            #Grab the individual players
            for player in team.parent.parent.parent.find_all('a', href=re.compile('/cbb/players/.')):

                content = player.parent.parent.contents

                minutes_played = int(content[3].text)
                field_goals = int(content[5].text)
                field_goal_attempts = int(content[7].text)
                field_goal_percentage = Decimal(content[9].text) if content[9].text is not '' else Decimal(1.0)
                two_point_field_goals = int(content[11].text)
                two_point_field_goal_attempts = int(content[13].text)
                two_point_field_goal_percentage = Decimal(content[15].text) if content[15].text is not '' else Decimal(1.0)
                three_point_field_goals = int(content[17].text)
                three_point_field_goal_attempts = int(content[19].text)
                three_point_field_goal_percentage = Decimal(content[21].text) if content[21].text is not '' else Decimal(1.0)
                free_throws = int(content[23].text)
                free_throw_attempts = int(content[25].text)
                free_throw_percentage = Decimal(content[27].text) if content[27].text is not '' else Decimal(1.0)
                offensive_rebounds = int(content[29].text)
                defensive_rebounds = int(content[31].text)
                total_rebounds = int(content[33].text)
                assists = int(content[35].text)
                steals = int(content[37].text)
                blocks = int(content[39].text)
                turnovers = int(content[41].text)
                personal_fouls = int(content[43].text)
                points = int(content[45].text)

                # Need to include player id
                playerStats.append(PlayerBoxScore(minutes_played, field_goals, field_goal_attempts, field_goal_percentage, 
                                                  two_point_field_goals, two_point_field_goal_attempts, 
                                                  two_point_field_goal_percentage, three_point_field_goals, 
                                                  three_point_field_goal_attempts, three_point_field_goal_percentage, 
                                                  free_throws, free_throw_attempts, free_throw_percentage, offensive_rebounds, 
                                                  defensive_rebounds, total_rebounds, assists, steals, blocks, turnovers,
                                                  personal_fouls, points))


        return playerStats
