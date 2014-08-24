from lib.scrapers.ign_scraper import IgnScraper


def test_ign_scraper_valid_game():
    s = IgnScraper('fallout new vegas')
    s.scrape()
    for attr in s._item.attributes:
        assert not attr.value is None