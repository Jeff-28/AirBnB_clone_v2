#!/usr/bin/python3
""" Module of the State class """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from os import getenv


class State(BaseModel, Base):
    """ Implementation for the State """

    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", passive_deletes=True, backref="state")
    else:
        name = ""

        @property
        def cities(self):
            '''Getter for cities'''
            cities = [value for key, value in models.storage.all().items()
                      if 'City' in key and value.state_id == self.id]
            return cities

    def __init__(self, *args, **kwargs):
        """Instantiates a State object"""
        super().__init__(*args, **kwargs)
