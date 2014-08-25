from lib.scrapers.gamespot_scraper import GamespotScraper
from lib.scrapers.ign_scraper import IgnScraper


class AllScraper(object):
    def __init__(self, game):
        self._game = game

    def scrape(self):
        values = list()
        values.append(IgnScraper(self._game).scrape())
        values.append(GamespotScraper(self._game).scrape())
        return values
