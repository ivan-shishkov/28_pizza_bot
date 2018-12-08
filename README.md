# Telegram Bot for Pizzeria

This bot allows you to display pizzeria menus based on data stored in the SQLite database.
Data is loaded into the database from the JSON file.
In addition, there is a convenient admin interface to manage the contents of the database.

# Quickstart

For service launch on localhost need to install Python 3.5 and then install all dependencies:

```bash

$ pip install -r requirements.txt

```

## Used Environment Variables

* **DATABASE_URI** - a database URI
* **SECRET_KEY** - a secret key for Flask application
* **BASIC_AUTH_USERNAME** - a username for login to admin interface
* **BASIC_AUTH_PASSWORD** - a password for login to admin interface
* **BOT_TOKEN** - a telegram bot token

## Database Creation

To create a database, you must specify its URI:

```bash

$ export DATABASE_URI='sqlite:///pizza_shop.sqlite'

```

and launch the script:

```bash

$ python3 db.py

```

## Loading Data into The Database

To load data to the database you need to run:

```bash

$ python3 load_to_db.py --filepath pizzas_info.json

```

## Admin Interface Launch

To launch the administrator interface, you must specify the secret key and data for authorization:

```bash

$ export SECRET_KEY='your_secret_key'
$ export BASIC_AUTH_USERNAME='your_username'
$ export BASIC_AUTH_PASSWORD='your_password'

```

and launch the script:

```bash

$ python3 server.py

```

Then open page [localhost:5000/admin](http://localhost:5000/admin) in browser.

## Telegram Bot Launch

Step 1. Register new telegram bot for development purposes, get the new token. [@BotFather](https://telegram.me/botfather)

Step 2. Launch

```bash

$ export BOT_TOKEN='your_bot_token'
$ python3 bot.py

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
