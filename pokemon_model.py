# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Pokemon(Base):
    __tablename__ = 'pokemon'

    id = Column(Integer, primary_key=True)
    pokemon_name = Column(String(100))
    species = Column(String(500))
    abilities = Column(String(500))
    moves = Column(String(1000))
    weight = Column(String(500))
    hieght = Column(String(500))
    forms = Column(String(1000))
    type = Column(String(500))
