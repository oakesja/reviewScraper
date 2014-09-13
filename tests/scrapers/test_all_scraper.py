from lib.scrapers.all_scraper import AllScraper


def test_average_rating(normal_reviews):
    x = AllScraper('test')
    avg = x.get_average_rating(normal_reviews)
    assert avg == 8.75


def test_average_rating_review_missing_one(missing_rating_review):
    x = AllScraper('test')
    avg = x.get_average_rating(missing_rating_review)
    assert avg == 9.0


def test_average_rating_review_missing_reviews(no_ratings_review):
    x = AllScraper('test')
    avg = x.get_average_rating(no_ratings_review)
    assert avg == "No Reviews"


def test_average_rating_review_missing_all():
    x = AllScraper('test')
    avg = x.get_average_rating([])
    assert avg == "No Reviews"


def test_average_community_rating(normal_reviews):
    x = AllScraper('test')
    avg = x.get_average_community_rating(normal_reviews)
    assert avg == 8.5


def test_average_community_rating_review_missing_one(missing_rating_review):
    x = AllScraper('test')
    avg = x.get_average_community_rating(missing_rating_review)
    assert avg == 8.0


def test_average_community_rating_review_missing_reviews(no_ratings_review):
    x = AllScraper('test')
    avg = x.get_average_community_rating(no_ratings_review)
    assert avg == "No Reviews"


def test_average_community_rating_review_missing_all():
    x = AllScraper('test')
    avg = x.get_average_community_rating([])
    assert avg == "No Reviews"


def test_get_reviews(review_scraper_mock):
    x = AllScraper('test')
    x._scrapers = [review_scraper_mock]
    x.get_reviews()
    assert x._reviews == [{"rating": "9.0"}]


def test_get_reviews_more_than_one(review_scraper_mock):
    x = AllScraper('test')
    x._scrapers = [review_scraper_mock, review_scraper_mock]
    x.get_reviews()
    assert x._reviews == [{"rating": "9.0"}, {"rating": "9.0"}]


def test_get_reviews_no_reviews(review_scraper_mock_none):
    x = AllScraper('test')
    x._scrapers = [review_scraper_mock_none]
    x.get_reviews()
    assert x._reviews == []


def test_get_description_both_valid(desc_scraper_mock_test, desc_scraper_mock_cover):
    x = AllScraper('test')
    x._ign_scraper = desc_scraper_mock_test
    x._gamespot_scraper = desc_scraper_mock_cover
    x.get_description()
    assert x._desc == {"cover": "cover"}


def test_get_description_only_ign(desc_scraper_mock_test, desc_scraper_mock_none):
    x = AllScraper('test')
    x._ign_scraper = desc_scraper_mock_test
    x._gamespot_scraper = desc_scraper_mock_none
    x.get_description()
    assert x._desc == {"cover": "test"}


def test_get_description_only_gamespot(desc_scraper_mock_test, desc_scraper_mock_none):
    x = AllScraper('test')
    x._ign_scraper = desc_scraper_mock_none
    x._gamespot_scraper = desc_scraper_mock_test
    x.get_description()
    assert x._desc == {"cover": "test"}


def test_get_description_missing_both(desc_scraper_mock_none):
    x = AllScraper('test')
    x._ign_scraper = desc_scraper_mock_none
    x._gamespot_scraper = desc_scraper_mock_none
    x.get_description()
    assert x._desc is None


