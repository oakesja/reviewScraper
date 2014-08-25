Review Scraper
============

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
