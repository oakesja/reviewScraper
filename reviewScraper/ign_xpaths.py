# TODO - make this immutable
class IgnXpaths(object):
    rating = "//*[contains(@class, 'ignRating ratingRow')]//*[contains(@class, 'ratingValue')]/text()"
    ratingDescription= "//*[contains(@class, 'ignRating ratingRow')]//*[contains(@class, 'ratingText')]/text()"
    communityRating = "//*[contains(@class, 'communityRating ratingRow')]//*[contains(@class, 'ratingValue')]/text()"
    communityRatingDescription = "//*[contains(@class, 'communityRating ratingRow')]//*[contains(@class, 'ratingText')]/text()"
    pictureLink = "//*[contains(@class, 'mainBoxArt')]/img/@src"
    reviewLink = "//*[contains(@class, 'ignRating ratingRow')]/a/@href"
    videoReviewLink = "//*[contains(@id, 'mainArticle')]//*[contains(@class, 'highlight-links clear')]/a/@href"
    esrbLink = "//*[contains(@id, 'summary')]/div[@class='gameInfo']/p/a/@href"