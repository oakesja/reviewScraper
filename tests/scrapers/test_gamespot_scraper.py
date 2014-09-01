from lib.scrapers.gamespot_scraper import GamespotScraper


def test_gamespot_scrape_review():
    s = GamespotScraper('fallout new vegas')
    d = s.scrape_review('dict')
    for key, value in d.iteritems():
        assert not value is None


def test_gamespot_scrape_description(gamespot_game_description):
    s = GamespotScraper('fallout new vegas')
    d = s.scrape_description('dict')
    assert d["game_name"] == 'Fallout: New Vegas'
    assert d["platform"] == 'Xbox 360, PlayStation 3, PC'
    assert d["release_date"] == 'Oct 19, 2010'
    assert d["game_description"] == gamespot_game_description
    assert d["genre"] == 'First-Person, Role-Playing'
    assert d['developer'] == 'Obsidian Entertainment'
    assert d['publisher'] == 'Bethesda Softworks, ZeniMax Media'
    assert d['picture_link'] is not None
    assert d['esrb_link'] is not None