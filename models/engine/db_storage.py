#!/usr/bin/python3
"""DBStorange for the HNBN project"""
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base


class DBStorage:
    """New engine"""
    __engine = None
    __session = None

    def __init__(self):
        """method init DBStorage"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB', 'localhost')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                        user, password,
                                        host, db,
                                        pool_pre_ping=True))

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''Show all the objects or a specific group'''
        list_objs = []
        if cls is None:
            list_objs += self.__session.query(State).all()
            list_objs += self.__session.query(City).all()

        else:
            list_objs = self.__session.query(cls).all()
        dict_objs = {}
        for obj in list_objs:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            dict_objs[key] = obj

        return dict_objs

    def new(self, obj):
        """add the object to the current database session """
        if obj:
            self.__session.add(obj)
            self.save()

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """reload session"""
        if self.__session:
            self.__session.close()

        Base.metadata.create_all(self.__engine)

        # create a new session
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Close the session"""
        self.__session.close()
