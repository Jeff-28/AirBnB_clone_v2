#!/usr/bin/python3
"""This module defines a class User"""
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import relationship
from sqlalchemy import Column, String, Integer, ForeignKey


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    reviews = relationship("Review", cascade="all, delete", backref="user")
    places = relationship("Place", cascade="all, delete", backref="user")
