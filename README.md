# Instawork Challenge - Members API

## Requirements
- python v3.12.6 (if using pyenv install with `pyenv install 3.12.6`)
- sqlite3

## Install
- pip install -r requirements.txt

## Setup
- `./manage.py migrate`

## Run the server
- `./manage.py runserver`

## Test
- Go to http://localhost:8000/members/ in your browser to access the API documentation,
- Use curl or postman GET/POST/PATCH/DELETE http://localhost:8000/members/, or
- Use the [Web UI app](https://github.com/juanc27/instawork-challenge-ui)

## Run unit tests
- `./manage.py test`

## Development
### Creating a module migration
- modify models.py
- `./manage.py makemigrations members`
- `./manage.py migrate`
