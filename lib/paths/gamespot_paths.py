# Review Information
def GamespotRatingXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' reviewObject__gs ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' gs-score__cell ')]//*[contains(concat(' ', normalize-space(@itemprop), ' '), 'ratingValue')]/text()"


def GamespotRatingDescriptionXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' reviewObject__meta ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' reviewObject__scoreWord ')]/text()"


def GamespotCommunityRatingXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' breakdown-userScore ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' breakdown-avgScore ')]//*[contains (concat(' ', normalize-space(@class), ' '), ' gs-score__cell ')]/text()"


def GamespotReviewLinkXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' media media-review ')][1]//a/@href"


# Game Information
def GamespotGameNameXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' gameObject__title ')]/a/text()"


def GamespotPlatformsXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' secondary-content ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' pod-objectStats-info__systems')]/ul/li/text()"


def GamespotReleaseDateXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' gameObject__info ')]//*[contains(concat(' ', normalize-space(@itemprop), ' '), ' datePublished ')]/text()"


def GamespotGameDescriptionXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' secondary-content ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' pod-objectStats-info__deck ')]/text()"


def GamespotGenre():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' secondary-content ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' pod-objectStats-additional ')]/dd[3]/a/text()"


def GamespotDeveloperXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' secondary-content ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' pod-objectStats-additional ')]/dd[1]/a/text()"


def GamespotPublisherXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' secondary-content ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' pod-objectStats-additional ')]/dd[2]/a/text()"


def GamespotPictureLinkXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' gameObject__img ')]//img/@src"


def GamespotEsrbLinkXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' secondary-content ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' pod-objectStats__esrb ')]/img/@src"


