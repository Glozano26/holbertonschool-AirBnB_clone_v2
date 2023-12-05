#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128) nullable=False)
    
    # DBStorage
    # the type of storage used
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', backref='state', cascade='all, delete')
        
    #FileStorage
    if getenv("HBNB_TYPE_STORAGE") is not None:
        @property
        def cities(self):
            """returns the list of City instances with state_id equals to the current State.id"""
            from models import storage
            from models.city import City
            
            all_cities = storage.all(City)
            
            list_cities = []
            for key, value in all_cities.items():
                if value.state_id == self.id:
                    list_cities.append(value)
            return list_cities
                    
                    
                    
                    
                    
                
            
    