import json

import requests

from lib.items.ignitem import IgnItem
from lib.xpaths import ignxpaths
from lib.loaders.ignitemloader import IgnItemLoader


class IgnRequester(object):
    def __init__(self, game):
        game = game.replace(' ', '-')
        self._url = 'http://www.ign.com/games/' + game
        self._item = IgnItem()

    def scrape_item(self):
        response = requests.get(self._url)
        l = IgnItemLoader(self._item)
        l.get_attr_from_xpath('rating', ignxpaths.rating, response)
        l.get_attr_from_xpath('ratingDescription', ignxpaths.ratingDescription, response)
        l.get_attr_from_xpath('communityRating', ignxpaths.communityRating, response)
        l.get_attr_from_xpath('communityDescripton', ignxpaths.communityRatingDescription, response)
        l.get_attr_from_xpath('boxArtLink', ignxpaths.pictureLink, response)
        l.get_attr_from_xpath('reviewLink', ignxpaths.reviewLink, response)
        l.get_attr_from_xpath('videoReviewLink', ignxpaths.videoReviewLink, response)
        l.get_attr_from_xpath('esrb', ignxpaths.esrbLink, response)

    def get_item_as_json(self):
        return json.dumps(self._item.__dict__)
