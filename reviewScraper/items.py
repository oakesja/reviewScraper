# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IgnItem(scrapy.Item):
    ignRating = scrapy.Field()
    ignDescription = scrapy.Field()
    communityRating = scrapy.Field()
    communityDescription = scrapy.Field()
    pictureLink = scrapy.Field()
    reviewLink = scrapy.Field()
    videoReviewLink = scrapy.Field()
    esrbLink = scrapy.Field()
    gameDescription = scrapy.Field()
