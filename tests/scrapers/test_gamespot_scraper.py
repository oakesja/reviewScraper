from lib.scrapers.gamespot_scraper import GamespotScraper


def test_ign_scraper_valid_game():
    s = GamespotScraper('fallout new vegas')
    s.scrape()
    for attr in s._item.attributes:
        assert not attr.value is None