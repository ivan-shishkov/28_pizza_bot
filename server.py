import os

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from db import PizzaType, PizzaChoice, db_session

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

admin = Admin(app, name='Pizza Shop', template_mode='bootstrap3')


class PizzaBaseModelView(ModelView):
    can_set_page_size = True


class PizzaTypeModelView(PizzaBaseModelView):
    column_searchable_list = ('title', 'description')
    column_labels = dict(title='Наименование', description='Описание')
    form_columns = ('title', 'description')


class PizzaChoiceModelView(PizzaBaseModelView):
    column_searchable_list = ('title',)
    column_labels = dict(pizza_type='Вид пиццы', title='Формат', price='Цена')


admin.add_view(PizzaTypeModelView(PizzaType, db_session, 'Виды пиццы'))
admin.add_view(PizzaChoiceModelView(PizzaChoice, db_session, 'Ассортимент'))

if __name__ == "__main__":
    app.run()
