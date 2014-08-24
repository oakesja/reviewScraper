reviewScraper
=============

Run tests with the following command:
'''
PYTHONPATH=. py.test tests
'''

Dependencies:
- requests
- lxml
- pytest
- mock

== Heroku ==
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