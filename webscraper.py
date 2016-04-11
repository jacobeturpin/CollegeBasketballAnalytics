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


    def get_individual_game_team_data(self):
        
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


    def get_individual_teams_game_stats(self):
        pass

    def get_individual_players_game_stats(self):
        pass
