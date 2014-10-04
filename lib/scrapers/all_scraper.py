import json

from lib.scrapers.gamespot_scraper import GamespotScraper
from lib.scrapers.ign_scraper import IgnScraper


class AllScraper(object):
    def __init__(self, game):
        self._ign_scraper = IgnScraper(game)
        self._gamespot_scraper = GamespotScraper(game)
        self._scrapers = [self._ign_scraper, self._gamespot_scraper]
        self._reviews = list()
        self._desc = None

    def scrape(self):
        output = dict()
        self.get_description()
        self.get_reviews()
        output["reviews"] = self._reviews
        output["description"] = self._desc
        output['averageRating'] = self.get_average_rating(self._reviews)
        output['averageCommunityRating'] = self.get_average_community_rating(self._reviews)
        return json.dumps(output)

    def get_description(self):
        self._desc = dict()
        self.update_desc(self._ign_scraper.scrape_description('dict'))
        self.update_desc(self._gamespot_scraper.scrape_description('dict'))
        if self._desc == {}:
            self._desc = None

    def update_desc(self, desc):
        if desc:
            self._desc.update(desc)

    def get_reviews(self):
        for scraper in self._scrapers:
            self.add_review(scraper.scrape_review('dict'))

    def add_review(self, review):
        if review:
            self._reviews.append(review)

    def get_average_rating(self, reviews):
        return self._get_average_rating(reviews, "rating")

    def get_average_community_rating(self, reviews):
        return self._get_average_rating(reviews, "communityRating")

    def _get_average_rating(self, reviews, rating_key):
        rating = 0
        count = 0
        for review in reviews:
            if rating_key in review:
                rating += float(review[rating_key])
                count += 1
        if count == 0:
            return "No Reviews"
        else:
            return '{:.3}'.format(rating / count)