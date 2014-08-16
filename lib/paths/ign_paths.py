def IgnRatingXpath():
    return "//*[contains(@class, 'ignRating ratingRow')]//*[contains(@class, 'ratingValue')]/text()"

def IgnRatingDescriptionXpath():
    return "//*[contains(@class, 'ignRating ratingRow')]//*[contains(@class, 'ratingText')]/text()"

def IgnCommunityRatingXpath():
    return "//*[contains(@class, 'communityRating ratingRow')]//*[contains(@class, 'ratingValue')]/text()"

def IgnCommunitRatingDescriptionXpath():
    return "//*[contains(@class, 'communityRating ratingRow')]//*[contains(@class, 'ratingText')]/text()"

def IgnPictureLinkXpath():
    return "//*[contains(@class, 'mainBoxArt')]/img/@src"

def IgnReviewLinkXpath():
    return "//*[contains(@class, 'ignRating ratingRow')]/a/@href"

def IgnVidoeReviewLinkXpath():
    return "//*[contains(@id, 'mainArticle')]//*[contains(@class, 'highlight-links clear')]/a/@href"

def IgnEsrbLinkXpath():
    return "//*[contains(@id, 'summary')]/div[@class='gameInfo']/p/a/@href"