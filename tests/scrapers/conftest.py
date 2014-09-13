import pytest

from mock import Mock


@pytest.fixture(scope="session")
def ign_game_description():
    return "Experience all the sights and sounds of fabulous New Vegas, " \
           "brought to you by Vault-Tec, America's First Choice in Post Nuclear " \
           "Simulation. Explore the treacherous wastes of the Great Southwest from" \
           " the safety and comfort of your very own vault: Meet new people, " \
           "confront terrifying creatures, and arm yourself with the latest " \
           "high-tech weaponry as you make a name for yourself on a thrilling " \
           "new journey across the Mojave wasteland. From Bethesda Softworks and " \
           "the veteran RPG designers at Obsidian Entertainment (a team which " \
           "includes members of the original Fallout and 2 teams) comes Fallout: " \
           "New Vegas, a thrilling and chilling episode in the Fallout saga."


@pytest.fixture(scope="session")
def gamespot_game_description():
    return "The latest game in the post-nuclear RPG series is being developed " \
           "by many members of the Fallout 1 and 2 team at Obsidian Entertainment " \
           "using the Fallout 3 engine."

@pytest.fixture(scope="session")
def normal_reviews():
    return [{"rating": "9.0", "communityRating": "8.0"}, {"rating": "8.5", "communityRating": "9.0"}]

@pytest.fixture(scope="session")
def missing_rating_review():
    return [{"rating": "9.0", "communityRating": "8.0"}, {"name": "test"}]

@pytest.fixture(scope="session")
def no_ratings_review():
    return [{"name": "foo"}, {"name": "test"}]

@pytest.fixture(scope="session")
def review_scraper_mock():
    scraper = Mock()
    scraper.scrape_review.return_value = dict(rating="9.0")
    return scraper

@pytest.fixture(scope="session")
def review_scraper_mock_none():
    scraper = Mock()
    scraper.scrape_review.return_value = None
    return scraper

@pytest.fixture(scope="session")
def desc_scraper_mock_test():
    scraper = Mock()
    scraper.scrape_description.return_value = dict(cover='test')
    return scraper

@pytest.fixture(scope="session")
def desc_scraper_mock_cover():
    scraper = Mock()
    scraper.scrape_description.return_value = dict(cover='cover')
    return scraper

@pytest.fixture(scope="session")
def desc_scraper_mock_none():
    scraper = Mock()
    scraper.scrape_description.return_value = None
    return scraper