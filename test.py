import webscraper

test = webscraper.WebScraperManager()


for i in range(10,13):
    games = test.get_all_games_for_date(month=1,day=i,year=2016)
    print(games, end='\n\n')
