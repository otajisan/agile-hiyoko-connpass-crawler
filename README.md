# agile-hiyoko-connpass-crawler
Agile hiyoko club connpass event page crawler

# Python Runtime Version

```bash
❱❱❱ python -V
Python 3.9.9
```

# Project making

- Create a virtual environment with [Pipenv]((https://pipenv.pypa.io/en/latest/)) so that you can use [Poetry](https://cocoatomo.github.io/poetry-ja/).

```bash
export PIPENV_VENV_IN_PROJECT=true
pipenv install --dev poetry
pipenv shell
```

- Then do the initial setup of the project by `poetry init`

```bash
❱❱❱ poetry init

This command will guide you through creating your pyproject.toml config.

Package name [agile-hiyoko-connpass-crawler]:
Version [0.1.0]:
Description []:  Agile hiyoko club connpass event page crawler
Author [otajisan <mtaji@morningcode.io>, n to skip]:  otajisan <mtaji@morningcode.io>
License []:
Compatible Python versions [^3.9]:

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "agile-hiyoko-connpass-crawler"
version = "0.1.0"
description = "Agile hiyoko club connpass event page crawler"
authors = ["otajisan <mtaji@morningcode.io>"]

[tool.poetry.dependencies]
python = "^3.9"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] yes
```

- finally, enable [scrapy](https://scrapy.org/) and [selenium](https://selenium-python.readthedocs.io/).

```bash
poetry add scrapy
poetry run scrapy startproject agile_hiyoko_connpass_crawler .
```

# How to start developing?

- setup `.envrc`

```bash
export CONNPASS_LOGIN_USER=<YOUR_CONNPASS_USERNAME or EMAIL>
export CONNPASS_LOGIN_PASS=<YOUR_CONNPASS_PASSWORD>
```

```bash
pipenv install
pipenv install --dev
pipenv shell
poetry install
brew install chromedriver
```

# How to execute?

```bash
❱❱❱ poetry run scrapy crawl connpass
2022-03-22 15:55:21 [scrapy.utils.log] INFO: Scrapy 2.6.1 started (bot: agile_hiyoko_connpass_crawler)
...
2022-03-22 15:55:43 [selenium.webdriver.remote.remote_connection] DEBUG: POST http://localhost:54296/session/c2bb140c17d097c606ffc925a5903317/url {"url": "https://connpass.com/event/242644/participants_csv/"}
2022-03-22 15:55:43 [urllib3.connectionpool] DEBUG: http://localhost:54296 "POST /session/c2bb140c17d097c606ffc925a5903317/url HTTP/1.1" 200 14
2022-03-22 15:55:43 [selenium.webdriver.remote.remote_connection] DEBUG: Finished Request
2022-03-22 15:55:46 [scrapy.core.scraper] DEBUG: Scraped from <200 https://agile-hiyoko-club.connpass.com/event/?page=1>
{'csv_url': 'https://connpass.com/event/242644/participants_csv/',
 'event_id': '242644',
 'name': 'アジャイルなマインドセットってどうやって身につけるの？',
 'url': 'https://agile-hiyoko-club.connpass.com/event/242644/'}
2022-03-22 15:55:46 [selenium.webdriver.remote.remote_connection] DEBUG: POST http://localhost:54296/session/c2bb140c17d097c606ffc925a5903317/url {"url": "https://connpass.com/event/238670/participants_csv/"}
2022-03-22 15:55:46 [urllib3.connectionpool] DEBUG: http://localhost:54296 "POST /session/c2bb140c17d097c606ffc925a5903317/url HTTP/1.1" 200 14
2022-03-22 15:55:46 [selenium.webdriver.remote.remote_connection] DEBUG: Finished Request
2022-03-22 15:55:49 [scrapy.core.scraper] DEBUG: Scraped from <200 https://agile-hiyoko-club.connpass.com/event/?page=1>
{'csv_url': 'https://connpass.com/event/238670/participants_csv/',
 'event_id': '238670',
 'name': 'どんなメトリクスをとって、どう活用している？',
 'url': 'https://agile-hiyoko-club.connpass.com/event/238670/'}
...
```

- After a few moments, the csv will be downloaded to the `csv` directory.

```bash
❱❱❱ ll csv | head
total 808
-rw-r--r--@ 1 mtaji  staff  10182  3 22 15:55 event_100104_participants.csv
-rw-r--r--@ 1 mtaji  staff  10843  3 22 15:57 event_106389_participants.csv
-rw-r--r--@ 1 mtaji  staff  11147  3 22 15:57 event_112987_participants.csv
-rw-r--r--@ 1 mtaji  staff  11735  3 22 15:57 event_121823_participants.csv
-rw-r--r--@ 1 mtaji  staff  13530  3 22 15:57 event_132109_participants.csv
-rw-r--r--@ 1 mtaji  staff  18451  3 22 15:56 event_136976_participants.csv
-rw-r--r--@ 1 mtaji  staff  10417  3 22 15:56 event_145516_participants.csv
-rw-r--r--@ 1 mtaji  staff  12351  3 22 15:56 event_152259_participants.csv
-rw-r--r--@ 1 mtaji  staff  14332  3 22 15:56 event_160465_participants.csv
```

# How to debug?

- for example, in the case of developing by [PyCharm](https://www.jetbrains.com/ja-jp/pycharm/), set the following


# How to add new spider?

```bash
poetry run scrapy genspider connpass connpass.com
```