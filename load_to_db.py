import os.path
import json
import argparse
import sys

from db import db_session, PizzaType, PizzaChoice


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file:
        return json.load(file)


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--filepath',
        help='a JSON file with pizzas info for load into the database '
             '(default value: pizzas_info.json)',
        default='pizzas_info.json',
        type=str,
    )
    command_line_arguments = parser.parse_args()

    return command_line_arguments


def get_pizza_choices(pizza_choices_info):
    return [
        PizzaChoice(**pizza_choice_info)
        for pizza_choice_info in pizza_choices_info
    ]


def load_to_database(pizzas_info):
    for pizza_info in pizzas_info:
        pizza_type = PizzaType(
            title=pizza_info['title'],
            description=pizza_info['description'],
        )
        pizza_type.choices = get_pizza_choices(pizza_info['choices'])

        db_session.add(pizza_type)

    db_session.commit()


def main():
    command_line_arguments = parse_command_line_arguments()

    filepath = command_line_arguments.filepath

    try:
        pizzas_info = load_json_data(filepath)
    except (UnicodeDecodeError, json.JSONDecodeError):
        sys.exit('JSON file has invalid format')

    if pizzas_info is None:
        sys.exit('JSON file not found')

    load_to_database(pizzas_info)


if __name__ == '__main__':
    main()
