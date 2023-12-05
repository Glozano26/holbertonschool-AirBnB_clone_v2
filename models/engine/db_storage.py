from sqlalchemy import create_engine
import os
from sqlalchemy import MetaData

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
        
        self.__engine = create_engine('mysql+mysqldb://'{}:{}@{}/{}'.format(
            user, password, host, db, pool_pre_ping=True)
            
        if env == 'test':
            metadata = MetaData(bind=self.__engine)
            metadata.drop_all()
            
    def all(self, cls=None):
        """Query on the current database session"""
        if cls:
            for obj in self.__session.query.(cls).all():
               
        
        
    