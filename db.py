import os

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.environ.get('DATABASE_URI'))

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()


class PizzaType(Base):
    __tablename__ = 'pizza_types'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False, unique=True)
    description = Column(String(200), nullable=False)

    choices = relationship(
        'PizzaChoice',
        back_populates='pizza_type',
        cascade='all',
        lazy='joined',
    )

    def __str__(self):
        return self.title


class PizzaChoice(Base):
    __tablename__ = 'pizza_choices'

    id = Column(Integer, primary_key=True)
    title = Column(String(20), nullable=False)
    price = Column(Integer, nullable=False)
    pizza_type_id = Column(Integer, ForeignKey('pizza_types.id'))
    pizza_type = relationship('PizzaType', back_populates='choices')


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
