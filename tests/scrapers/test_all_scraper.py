from lib.scrapers.all_scraper import AllScraper


def test_average_rating(normal_reviews):
    x = AllScraper('test')
    avg = x.get_average_rating(normal_reviews)
    assert avg == 8.75


def test_average_rating_review_missing_one(missing_rating_review):
    x = AllScraper('test')
    avg = x.get_average_rating(missing_rating_review)
    assert avg == 9.0


def test_average_rating_review_missing_all(no_ratings_review):
    x = AllScraper('test')
    avg = x.get_average_rating(no_ratings_review)
    assert avg == 0


def test_average_community_rating(normal_reviews):
    x = AllScraper('test')
    avg = x.get_average_community_rating(normal_reviews)
    assert avg == 8.5


def test_average_community_rating_review_missing_one(missing_rating_review):
    x = AllScraper('test')
    avg = x.get_average_community_rating(missing_rating_review)
    assert avg == 8.0


def test_average_community_rating_review_missing_all(no_ratings_review):
    x = AllScraper('test')
    avg = x.get_average_community_rating(no_ratings_review)
    assert avg == 0
