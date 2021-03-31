#!/usr/bin/python3
"""This module defines a class User"""
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        reviews = relationship("Review", cascade="all, delete", backref="user")
        places = relationship("Place", cascade="all, delete", backref="user")
    else:
        first_name = ""
        last_name = ""
        password = ""
        email = ""

    def __init__(self, *args, **kwargs):
        """Instantiates a User object"""
        super().__init__(*args, **kwargs)
