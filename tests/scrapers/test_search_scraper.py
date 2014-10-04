from lib.scrapers.search_scraper import SearchScraper


def test_search_scraper():
    results = SearchScraper("fallout").scrape_results('dict')
    assert len(results) == 9
    assert results[0]["gameName"] == "Fallout"
    assert results[0]["pictureLink"] == "http://macmedia.ign.com/mac/image/object/003/003512/689365boxart_160w.jpg"
    assert results[0]["lookupKey"] == "fallout"
    assert results[0]["platforms"] == "by Interplay for Mac, PC"
