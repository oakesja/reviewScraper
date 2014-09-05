from lib.scrapers.gamespot_scraper import GamespotScraper


def test_gamespot_scrape_review():
    s = GamespotScraper('fallout new vegas')
    d = s.scrape_review('dict')
    for key, value in d.iteritems():
        assert not value is None


def test_gamespot_scrape_description(gamespot_game_description):
    s = GamespotScraper('fallout new vegas')
    d = s.scrape_description('dict')
    assert d["gameName"] == 'Fallout: New Vegas'
    assert d["platform"] == 'Xbox 360, PlayStation 3, PC'
    assert d["releaseDate"] == 'Oct 19, 2010'
    assert d["gameDescription"] == gamespot_game_description
    assert d["genre"] == 'First-Person, Role-Playing'
    assert d['developer'] == 'Obsidian Entertainment'
    assert d['publisher'] == 'Bethesda Softworks, ZeniMax Media'
    assert d['pictureLink'] is not None
    assert d['esrbLink'] is not None