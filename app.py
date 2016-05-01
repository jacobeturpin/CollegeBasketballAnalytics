from boxscore import * 
from databasemanager import DatabaseManager
from webscraper import WebScraperManager
import statistics
from config import *

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


if __name__ == '__main__':
    #database_manager = DatabaseManager()
    #web_scraper = WebScraperManager()

    app.run()