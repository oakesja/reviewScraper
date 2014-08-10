import scrapy

from reviewScraper.items import IgnItem
from reviewScraper.ign_xpaths import IgnXpaths
from reviewScraper.itemLoaders.ignItemLoader import IgnItemLoader

class IgnReviewSpider(scrapy.Spider):
    name = "ign"
    allowed_domains = ["ign.com"]
    start_urls = [
        "http://www.ign.com/games/fallout-new-vegas"
    ]

    def parse(self, response):
        paths = IgnXpaths()
        item = IgnItem()
        il = IgnItemLoader(item=IgnItem(), response=response)
        il.add_xpath('ignRating', paths.rating)
        il.add_xpath('ignDescription', paths.ratingDescription)
        il.add_xpath('communityRating', paths.communityRating)
        il.add_xpath('communityDescription', paths.communityRatingDescription)
        il.add_xpath('pictureLink', paths.pictureLink)
        il.add_xpath('reviewLink', paths.reviewLink)
        il.add_xpath('videoReviewLink', paths.videoReviewLink)
        il.add_xpath('esrbLink', paths.esrbLink)
        yield il.load_item()
