from lib.scrapers.ign_scraper import IgnScraper


def test_ign_scrape_review():
    s = IgnScraper('fallout new vegas')
    d = s.scrape_review('dict')
    for key, value in d.iteritems():
        assert not value is None


def test_ign_scrape_description(ign_game_description):
    s = IgnScraper('fallout new vegas')
    d = s.scrape_description('dict')
    assert d["game_name"] == 'Fallout: New Vegas'
    assert d["platform"] == 'PC, PS3, Xbox 360'
    assert d["release_date"] == 'October 19. 2010'
    assert d["game_description"] == ign_game_description
    assert d["genre"] == 'RPG'
    assert d['developer'] == 'Obsidian Entertainment'
    assert d['publisher'] == 'Bethesda  Softworks'
    assert d['picture_link'] is not None
    assert d['esrb_link'] is not None