#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenity = Table('place_amenities', Base.metadata,
                      