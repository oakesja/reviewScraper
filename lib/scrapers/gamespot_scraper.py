import requests
import logging

from lib.paths.gamespot_paths import *
from lib.utils.item import Item
from lib.utils.formatters import take_all, take_all_comma, gamespot_review_link


class GamespotScraper(object):
    def __init__(self, game):
        game = game.replace(' ', '-').lower()
        self._url = 'http://www.gamespot.com/' + game + '/reviews'
        self._review_item = Item('Gamespot')
        self._desc_item = Item()
        self._logger = logging.getLogger(__name__)
        self._response = None

    def scrape_review(self, export_type='json'):
        self._logger.info('Scraping review %s', self._url)
        self._response = self._response or requests.get(self._url)
        self._review_item.add_xpath_attribute(self._response, 'rating', GamespotRatingXpath())
        self._review_item.add_xpath_attribute(self._response, 'ratingDescription', GamespotRatingDescriptionXpath())
        self._review_item.add_xpath_attribute(self._response, 'communityRating', GamespotCommunityRatingXpath())
        self._review_item.add_xpath_attribute(self._response, 'reviewLink', GamespotReviewLinkXpath(), gamespot_review_link)
        return self._review_item.export(export_type)

    def scrape_description(self, export_type='json'):
        self._logger.info('Scraping description %s', self._url)
        self._response = self._response or requests.get(self._url)
        self._desc_item.add_xpath_attribute(self._response, 'gameName', GamespotGameNameXpath())
        self._desc_item.add_xpath_attribute(self._response, 'platform', GamespotPlatformsXpath(), take_all_comma)
        self._desc_item.add_xpath_attribute(self._response, 'releaseDate', GamespotReleaseDateXpath())
        self._desc_item.add_xpath_attribute(self._response, 'gameDescription', GamespotGameDescriptionXpath(), take_all)
        self._desc_item.add_xpath_attribute(self._response, 'genre', GamespotGenre(), take_all_comma)
        self._desc_item.add_xpath_attribute(self._response, 'developer', GamespotDeveloperXpath(), take_all_comma)
        self._desc_item.add_xpath_attribute(self._response, 'publisher', GamespotPublisherXpath(), take_all_comma)
        self._desc_item.add_xpath_attribute(self._response, 'pictureLink', GamespotPictureLinkXpath())
        self._desc_item.add_xpath_attribute(self._response, 'esrbLink', GamespotEsrbLinkXpath())
        return self._desc_item.export(export_type)


