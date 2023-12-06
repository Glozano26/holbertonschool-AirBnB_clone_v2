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
        """Query on the current database session"""
        dic = {}
        if cls:
            for obj in self.__session.query(cls).all():
                dic[type(obj).__name__ + '.' + obj.id] = obj
        else:
            for cls in [City, State, User, Place, Amenity, Review]:
                for obj in self.__session.query(cls).all():
                    dic[type(obj).__name__ + '.' + obj.id] = obj
        return dic


    def new(self, obj):
        """add the object to the current database session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """reload session"""
        Base.metadata.create_all(self.__engine)

        # create a new session
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Close the session"""
        self.__session.close()
