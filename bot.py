import telebot
from jinja2 import Template
from os import getenv

from db import db_session, PizzaType

TOKEN = getenv('BOT_TOKEN')
if not TOKEN:
    raise Exception('BOT_TOKEN should be specified')

bot = telebot.TeleBot(TOKEN)

with open('templates/catalog.md', 'r') as catalog_file:
    catalog_template = Template(catalog_file.read())

with open('templates/greetings.md', 'r') as greetings_file:
    greetings_template = Template(greetings_file.read())


@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, greetings_template.render())


@bot.message_handler(commands=['menu'])
def show_catalog(message):
    catalog = db_session.query(PizzaType).all()
    bot.send_message(
        message.chat.id,
        catalog_template.render(catalog=catalog),
        parse_mode='Markdown',
    )


if __name__ == '__main__':
    bot.polling(none_stop=True)
