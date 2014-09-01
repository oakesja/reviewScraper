# Review Information
def IgnRatingXpath():
    return "//*[contains(@class, 'ignRating ratingRow')]//*[contains(@class, 'ratingValue')]/text()"


def IgnRatingDescriptionXpath():
    return "//*[contains(@class, 'ignRating ratingRow')]//*[contains(@class, 'ratingText')]/text()"


def IgnCommunityRatingXpath():
    return "//*[contains(@class, 'communityRating ratingRow')]//*[contains(@class, 'ratingValue')]/text()"


def IgnCommunitRatingDescriptionXpath():
    return "//*[contains(@class, 'communityRating ratingRow')]//*[contains(@class, 'ratingText')]/text()"


def IgnReviewLinkXpath():
    return "//*[contains(@class, 'ignRating ratingRow')]/a/@href"


def IgnVidoeReviewLinkXpath():
    return "//*[contains(@id, 'mainArticle')]//*[contains(@class, 'highlight-links clear')]/a/@href"


# Game Information
def IgnGameNameXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' contentTitle ')]/a/text()"


def IgnPlatformXpaths():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' contentPlatformsText ')]/span/a/text()"


def IgnReleaseDateXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' releaseDate ')]/strong/text()"


def IgnGameDescriptionXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' gameInfo ')]/p/text()"


def IgnGenre():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' gameInfo-list ')][2]/div[1]/a/text()"


def IgnDeveloperXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' gameInfo-list ')][2]/div[3]/a/text()"


def IgnPublisherXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' gameInfo-list ')][2]/div[2]/a/text()"


def IgnPictureLinkXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' mainBoxArt ')]/img/@src"


def IgnEsrbLinkXpath():
    return "//*[contains(@id, 'summary')]/div[@class='gameInfo']/p/a/@href"


