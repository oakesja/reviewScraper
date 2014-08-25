Review Scraper
============
[ ![Codeship Status for oakesja/reviewScraper](https://www.codeship.io/projects/69f53e70-0eb3-0132-d7c4-1276fda57f98/status?branch=master)](https://www.codeship.io/projects/32485)
[![Codacy Badge](https://www.codacy.com/project/badge/9680c9b6bd174ccaa7d650b2389d0e06)](https://www.codacy.com)


## Tests ##
Tests are stored in the `tests` directory. They are written using pytest and mock.

Run tests with the following command:
```
PYTHONPATH=. py.test tests
```

## Heroko ##
Update requirements: 
```
ENV/bin/pip freeze > requirements.txt
```
Start application:
```
git push heroku master
```
Check processes:
```
heroku ps
```
Check logs:
```
heroku logs
```
