import requests
from lib.paths.gamespot_paths import *
from lib.utils.item import Item


class GamespotScraper(object):
    def __init__(self, game):
        game = game.replace(' ', '-')
        self._url = 'http://www.gamespot.com/' + game + '/reviews'
        self._item = Item('Gamespot')

    def scrape(self):
        response = requests.get(self._url)
        self._item.add_xpath_attribute(response, 'rating', GamespotRatingXpath())
        return self._item.export()

