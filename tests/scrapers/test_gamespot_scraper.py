from lib.scrapers.gamespot_scraper import GamespotScraper


def test_gamespot_scrape_review():
    s = GamespotScraper('fallout new vegas')
    d = s.scrape_review('dict')
    assert d["rating"] is not None
    assert d["communityRating"] is not None
    assert d["ratingDescription"] is not None
    assert d["reviewLink"] == 'http://www.gamespot.com/reviews/fallout-new-vegas-review/1900-6282605/'


def test_gamespot_scrape_description(gamespot_game_description):
    s = GamespotScraper('fallout new vegas')
    d = s.scrape_description('dict')
    assert d["gameName"] == 'Fallout: New Vegas'
    assert d["platform"] == 'PC, PlayStation 3, Xbox 360'
    assert d["releaseDate"] == 'Oct 19, 2010'
    assert d["gameDescription"] == gamespot_game_description
    assert 'Role-Playing' in d["genre"]
    assert 'First-Person' in d["genre"]
    assert d['developer'] == 'Obsidian Entertainment'
    assert d['publisher'] == 'Bethesda Softworks, ZeniMax Media'
    assert d['pictureLink'] is not None
    assert d['esrbLink'] is not None

