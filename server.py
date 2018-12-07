import os

from flask import Flask
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth

from db import PizzaType, PizzaChoice, db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)


class PizzaAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not basic_auth.authenticate():
            return basic_auth.challenge()

        return super(PizzaAdminIndexView, self).index()


class PizzaBaseModelView(ModelView):
    can_set_page_size = True

    def is_accessible(self):
        if not basic_auth.authenticate():
            return False

        return True


class PizzaTypeModelView(PizzaBaseModelView):
    column_searchable_list = ('title', 'description')
    column_labels = dict(title='Наименование', description='Описание')
    form_columns = ('title', 'description')


class PizzaChoiceModelView(PizzaBaseModelView):
    column_searchable_list = ('title',)
    column_labels = dict(pizza_type='Вид пиццы', title='Формат', price='Цена')


admin = Admin(
    app,
    name='Пиццерия',
    template_mode='bootstrap3',
    index_view=PizzaAdminIndexView(name='Главная'),
)
admin.add_view(PizzaTypeModelView(PizzaType, db_session, 'Виды пиццы'))
admin.add_view(PizzaChoiceModelView(PizzaChoice, db_session, 'Ассортимент'))

if __name__ == "__main__":
    app.run()
