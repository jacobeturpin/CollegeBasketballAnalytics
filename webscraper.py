import requests, datetime
from bs4 import BeautifulSoup


class WebScraperManager():

    _url_root = 'http://sports-reference.com/cbb/'

    def __init__(self):
        return None

    def get_all_games_for_date(self, month, day, year):

        if datetime.datetime.today() < datetime.datetime(month=month, day=day, year=year):
            raise

        url = str.format('{0}boxscores/index.cgi?month={1}&day={2}&year={3}',
                         self._url_root,
                         month,
                         day,
                         year)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        games = []
        for link in soup.find_all('a', text='Final'):
            games.append(link.get('href'))
        return games


    def get_individual_game_data(self, game_link_address):
        r = requests.get(str.format('{0}{1}', _url_root, game_link_address))
        soup = BeautifulSoup(r.content, "html.parser")

        teams = self.get_individual_game_team_data(soup)
        team_stats = self.get_individual_teams_game_stats(soup, teams)
        player_stats = self.get_individual_players_game_stats(soup, teams)

        return {'teams': teams, 'teamStats': team_stats, 'playerStats': player_stats}


    def get_individual_game_team_data(self, soup):
        
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
    def get_individual_teams_game_stats(self, soup, teams):
        
        i, teamStats = 0, []
        staging = soup.find_all('th', text='Basic Box Score Stats')
        content = [x.parent.find_next('td', text='School Totals').parent.find_all('td')[1:] for x in staging]
        
        for team in teams:
            i += 1 

            minutesPlayed = int(content[i-1][0].text)
            fieldGoals = int(content[i-1][1].text)
            fieldGoalAttempts = int(content[i-1][2].text)
            fieldGoalPercentage = Decimal(content[i-1][3].text)
            twoPointFieldGoals = int(content[i-1][4].text)
            twoPointFieldGoalAttempts = int(content[i-1][5].text)
            twoPointFieldGoalPercentage = Decimal(content[i-1][6].text)
            threePointFieldGoals = int(content[i-1][7].text)
            threePointFieldGoalAttempts = int(content[i-1][8].text)
            threePointFieldGoalPercentage = Decimal(content[i-1][9].text)
            freeThrows = int(content[i-1][10].text)
            freeThrowAttempts = int(content[i-1][11].text)
            freeThrowPercentage = Decimal(content[i-1][12].text)
            offensiveRebounds = int(content[i-1][13].text)
            defensiveRebounds = int(content[i-1][14].text)
            totalRebounds = int(content[i-1][15].text)
            assists = int(content[i-1][16].text)
            steals = int(content[i-1][17].text)
            blocks = int(content[i-1][18].text)
            turnovers = int(content[i-1][19].text)
            personalFouls = int(content[i-1][20].text)
            points = int(content[i-1][21].text)

            teamStats.append({
                    'teamName': teams[0]['teamName'] if i % 2 == 1 else teams[1]['teamName'],
                    'seasonYear': 2016,
                    'gameDate': date(month=12,day=12,year=2012),
                    'minutesPlayed': minutesPlayed if minutesPlayed is not '' else 5,
                    'fieldGoals': fieldGoals if fieldGoals is not '' else 5,
                    'fieldGoalAttempts': fieldGoalAttempts if fieldGoalAttempts is not '' else 5,
                    'fieldGoalPercentage': fieldGoalPercentage if fieldGoalPercentage is not '' else 5,
                    'twoPointFieldGoals': twoPointFieldGoals if twoPointFieldGoals is not '' else 5,
                    'twoPointFieldGoalAttempts': twoPointFieldGoalAttempts if twoPointFieldGoalAttempts is not '' else 5,
                    'twoPointFieldGoalPercentage': twoPointFieldGoalPercentage if twoPointFieldGoalPercentage is not '' else 5,
                    'threePointFieldGoals': threePointFieldGoals if threePointFieldGoals is not '' else 5,
                    'threePointFieldGoalAttempts': threePointFieldGoalAttempts if threePointFieldGoalAttempts is not '' else 5,
                    'threePointFieldGoalPercentage': threePointFieldGoalPercentage if threePointFieldGoalPercentage is not '' else 5,
                    'freeThrows': freeThrows if freeThrows is not '' else 5,
                    'freeThrowAttempts': freeThrowAttempts if freeThrowAttempts is not '' else 5,
                    'freeThrowPercentage': freeThrowPercentage if freeThrowPercentage is not '' else 5,
                    'offensiveRebounds': offensiveRebounds if offensiveRebounds is not '' else 5,
                    'defensiveRebounds': defensiveRebounds if defensiveRebounds is not '' else 5,
                    'totalRebounds': totalRebounds if totalRebounds is not '' else 5,
                    'assists': assists if assists is not '' else 5,
                    'steals': steals if steals is not '' else 5,
                    'blocks': blocks if blocks is not '' else 5,
                    'turnovers': turnovers if turnovers is not '' else 5,
                    'personalFouls': personalFouls if personalFouls is not '' else 5,
                    'points': points if points is not '' else 5,

                    # Advanced (Calculated) Metrics
                    'trueShootingPercentage': calculateTrueShootingPercentage(points, fieldGoalAttempts, freeThrowAttempts),
                    'effectiveFieldGoalPercentage': calculateEffectiveFieldGoalPercentage(fieldGoals, threePointFieldGoals, fieldGoalAttempts),
                    'threePointAttemptRate': calculateThreePointAttemptRate(threePointFieldGoalAttempts, fieldGoalAttempts),
                    'freeThrowAttemptRate': calculateFreeThrowAttemptRate(freeThrowAttempts, fieldGoalAttempts),
                    'offensiveReboundingPercentage': calculateOffensiveReboundingPercentage(),
                    'defensiveReboundingPercentage': calculateDefensiveReboundingPercentage(),
                    'totalReboundingPercentage': calculateTotalReboundingPercentage(),
                    'assistPercentage': calculateAssistPercentage(),
                    'stealPercentage': calculateStealPercentage(),
                    'blockPercentage': calculateBlockPercentage(),
                    'turnoverPercentage': calculateTurnoverPercentage(),
                    'usagePercentage': calculateUsagePercentage(),
                    'offensiveRating': calculateOffensiveRating(),
                    'defensiveRating': calculateDefensiveRating()
                    })

        return teamStats

    # Need to make tolerant of null statistical categories
    def get_individual_players_game_stats(self):
        pass
