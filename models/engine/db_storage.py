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
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class DBStorage:
    """New engine"""
    __engine = None
    __session = None

    def __init__(self):
        """method init DBStorage"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                        user, password,
                                        host, db), pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''Show all the objects or a specific group'''
        list_objs = []
        if cls is None:
            list_objs += self.__session.query(User).all()
            list_objs += self.__session.query(State).all()
            list_objs += self.__session.query(City).all()
            list_objs += self.__session.query(Amenity).all()
            list_objs += self.__session.query(Place).all()
            list_objs += self.__session.query(Review).all()
        else:
            list_objs = self.__session.query(cls).all()
        dict_objs = {}
        for obj in list_objs:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            dict_objs[key] = obj
            # dict_objs[obj.__class__.__name__ + "." + obj.id](obj)
        return dict_objs

    def new(self, obj):
        """add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        self.__session.delete(obj)

    def reload(self):
        """reload session"""

        Base.metadata.create_all(self.__engine)

        # create a new session
        s_tmp = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_tmp)
        self.__session = Session()

    def close(self):
        """Close the session working SQLAlchemy"""
        self.__session.close()
