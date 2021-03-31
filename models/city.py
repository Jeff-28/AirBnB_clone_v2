#!/usr/bin/python3
""" Define the class City """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ Define the class City that inherits from BaseModel """

    __tablename__ = 'cities'
    if getenv('HBNB_STORAGE_TYPE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", cascade="all, delete", backref="cities")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """Class constructor"""
        super().__init__(*args, **kwargs)
