def GamespotRatingXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' reviewObject__gs ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' gs-score__cell ')]//*[contains(concat(' ', normalize-space(@itemprop), ' '), 'ratingValue')]/text()"


def GamespotRatingDescriptionXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' reviewObject__meta ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' reviewObject__scoreWord ')]/text()"


def GamespotCommunityRatingXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' breakdown-userScore ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' breakdown-avgScore ')]//*[contains (concat(' ', normalize-space(@class), ' '), ' gs-score__cell ')]/text()"


def GamespotPictureLinkXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' gameObject__img ')]//img/@src"


def GamespotReviewLinkXpath():
    return "//*[contains(concat(' ', normalize-space(@class), ' '), ' media media-review ')][1]//a/@href"
