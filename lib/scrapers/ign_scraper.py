import requests
import logging

from lib.paths.ign_paths import *
from lib.utils.item import Item
from lib.utils.formatters import take_all_comma, take_all


class IgnScraper(object):
    def __init__(self, game):
        game = game.replace(' ', '-').lower()
        self._url = 'http://www.ign.com/games/' + game
        self._review_item = Item('IGN')
        self._desc_item = Item()
        self._logger = logging.getLogger(__name__)
        self._response = None

    def scrape_review(self, export_type='json'):
        self._logger.info('Scraping review %s', self._url)
        self._response = self._response or requests.get(self._url)
        self._review_item.add_xpath_attribute(self._response, 'rating', IgnRatingXpath())
        self._review_item.add_xpath_attribute(self._response, 'rating_description', IgnRatingDescriptionXpath())
        self._review_item.add_xpath_attribute(self._response, 'community_rating', IgnCommunityRatingXpath())
        self._review_item.add_xpath_attribute(self._response, 'community_rating_description', IgnCommunitRatingDescriptionXpath())
        self._review_item.add_xpath_attribute(self._response, 'review_link', IgnReviewLinkXpath())
        self._review_item.add_xpath_attribute(self._response, 'video_review_link', IgnVidoeReviewLinkXpath())
        return self._review_item.export(export_type)

    def scrape_description(self, export_type='json'):
        self._logger.info('Scraping description %s', self._url)
        self._response = self._response or requests.get(self._url)
        self._desc_item.add_xpath_attribute(self._response, 'game_name', IgnGameNameXpath())
        self._desc_item.add_xpath_attribute(self._response, 'platform', IgnPlatformXpaths(), take_all_comma)
        self._desc_item.add_xpath_attribute(self._response, 'release_date', IgnReleaseDateXpath())
        self._desc_item.add_xpath_attribute(self._response, 'game_description', IgnGameDescriptionXpath(), take_all)
        self._desc_item.add_xpath_attribute(self._response, 'genre', IgnGenre(), take_all_comma)
        self._desc_item.add_xpath_attribute(self._response, 'developer', IgnDeveloperXpath(), take_all_comma)
        self._desc_item.add_xpath_attribute(self._response, 'publisher', IgnPublisherXpath(), take_all_comma)
        self._desc_item.add_xpath_attribute(self._response, 'picture_link', IgnPictureLinkXpath())
        self._desc_item.add_xpath_attribute(self._response, 'esrb_link', IgnEsrbLinkXpath())
        return self._desc_item.export(export_type)