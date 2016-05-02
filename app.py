from boxscore import * 
from databasemanager import DatabaseManager
from webscraper import WebScraperManager
import statistics
from config import *

from server import app

if __name__ == '__main__':
    #database_manager = DatabaseManager()
    #web_scraper = WebScraperManager()

    app.run(debug=True)