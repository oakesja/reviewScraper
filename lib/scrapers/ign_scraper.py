import requests

from lib.paths.ign_paths import *
from lib.utils.item import Item


class IgnScraper(object):
    def __init__(self, game):
        game = game.replace(' ', '-')
        self._url = 'http://www.ign.com/games/' + game
        self._item = Item('IGN')

    def scrape(self):
        response = requests.get(self._url)
        self._item.add_xpath_attribute(response, 'rating', IgnRatingXpath())
        self._item.add_xpath_attribute(response, 'rating_description', IgnRatingDescriptionXpath())
        self._item.add_xpath_attribute(response, 'community_rating', IgnCommunityRatingXpath())
        self._item.add_xpath_attribute(response, 'community_rating_description', IgnCommunitRatingDescriptionXpath())
        self._item.add_xpath_attribute(response, 'picture_link', IgnPictureLinkXpath())
        self._item.add_xpath_attribute(response, 'review_link', IgnReviewLinkXpath())
        self._item.add_xpath_attribute(response, 'video_review_link', IgnVidoeReviewLinkXpath())
        self._item.add_xpath_attribute(response, 'esrb_link', IgnEsrbLinkXpath())
        return self._item.export()
