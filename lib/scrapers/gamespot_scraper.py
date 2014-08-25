import requests
from lib.paths.gamespot_paths import *
from lib.utils.item import Item


class GamespotScraper(object):
    def __init__(self, game):
        game = game.replace(' ', '-')
        self._url = 'http://www.gamespot.com/' + game + '/reviews'
        self._item = Item('Gamespot')

    def scrape(self, export_type='json'):
        response = requests.get(self._url)
        self._item.add_xpath_attribute(response, 'rating', GamespotRatingXpath())
        self._item.add_xpath_attribute(response, 'rating_description', GamespotRatingDescriptionXpath())
        self._item.add_xpath_attribute(response, 'community_rating', GamespotCommunityRatingXpath())
        self._item.add_xpath_attribute(response, 'picture_link', GamespotPictureLinkXpath())
        self._item.add_xpath_attribute(response, 'review_link', GamespotReviewLinkXpath())
        return self._item.export(export_type)

