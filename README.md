# Instawork Challenge - Members API

## Requirements
- python v3.12.6 (if using pyenv install with `pyenv install 3.12.6`)
- sqlite3

## Install
- pip install -r requirements.txt

## Setup
- ./manage.py migrate

## Run the server
- ./manage.py runserver

## Development
### Creating a module migration
- modify models.py
- ./manage.py makemigrations <module>
- ./manage.py migrate <module>
