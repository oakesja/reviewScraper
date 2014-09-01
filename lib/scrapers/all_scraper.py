import json

from lib.scrapers.gamespot_scraper import GamespotScraper
from lib.scrapers.ign_scraper import IgnScraper


class AllScraper(object):
    def __init__(self, game):
        self._ign_scraper = IgnScraper(game)
        self._gamespot_scraper = GamespotScraper(game)

    def scrape(self):
        output = dict()
        reviews = list()
        reviews.append(self._ign_scraper.scrape_review('dict'))
        reviews.append(self._gamespot_scraper.scrape_review('dict'))
        descr = self._ign_scraper.scrape_description('dict')
        descr.update(self._gamespot_scraper.scrape_description('dict'))
        output["reviews"] = reviews
        output["description"] = descr
        output['average_rating'] = self.get_average_rating(reviews)
        output['average_community_rating'] = self.get_average_community_rating(reviews)
        return json.dumps(output)

    def get_average_rating(self, reviews):
        return self._get_average_rating(reviews, "rating")

    def get_average_community_rating(self, reviews):
        return self._get_average_rating(reviews, "community_rating")

    def _get_average_rating(self, reviews, rating_key):
        rating = 0
        count = 0
        for review in reviews:
            if rating_key in review:
                rating += float(review[rating_key])
                count += 1
        if count == 0:
            return 0
        else:
            return rating / count