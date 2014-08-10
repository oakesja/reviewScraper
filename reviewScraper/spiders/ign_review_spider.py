import scrapy

from reviewScraper.items import IgnItem
from reviewScraper.ign_xpaths import IgnXpaths

class IgnReviewSpider(scrapy.Spider):
    name = "ign"
    allowed_domains = ["ign.com"]
    start_urls = [
        "http://www.ign.com/games/fallout-new-vegas"
    ]
    

    def parse(self, response):
        paths = IgnXpaths()
        item = IgnItem()
        item['ignRating'] = response.xpath(paths.rating).extract()[0].strip()
        item['ignDescription'] = response.xpath(paths.ratingDescription).extract()[0].strip()
        item['communityRating'] = response.xpath(paths.communityRating).extract()[0].strip()
        item['communityDescription'] = response.xpath(paths.communityRatingDescription).extract()[0].strip()
        item['pictureLink'] = response.xpath(paths.pictureLink).extract()[0].strip()
        item['reviewLink'] = response.xpath(paths.reviewLink).extract()[0].strip()
        item['videoReviewLink'] = response.xpath(paths.videoReviewLink).extract()[0].strip()
        item['esrbLink'] = response.xpath(paths.esrbLink).extract()[0].strip()
        yield item