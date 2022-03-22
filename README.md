# agile-hiyoko-connpass-crawler
Agile hiyoko club connpass event page crawler

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

- finally, enable [scrapy](https://scrapy.org/)

```bash
poetry add scrapy
poetry run scrapy startproject agile_hiyoko_connpass_crawler .
```

# How to start developing?

```bash
pipenv install
pipenv shell
poetry install
brew install chromedriver
```

# How to debug?

```bash
poetry run scrapy crawl connpass
```

# How to add new spider?

```bash
poetry run scrapy genspider connpass connpass.com
```