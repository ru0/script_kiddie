# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from scrapy.utils.project import get_project_settings
import logging
logger = logging.getLogger(__name__)

Base = declarative_base()

def db_connect():
    settings = get_project_settings()
    mysql_db = settings.get('DATABASE')
    #logger.warning("<Ruo>")
    return create_engine(URL(**mysql_db))
    
def create_dy_table(engine):
    """ create tables """
    Base.metadata.create_all(engine)
  
class Dy(Base):
    """ table columns """
    __tablename__ = "dy2018"
  
    id = Column(Integer, primary_key=True)
    name = Column('name', String(1000))
    link = Column('link', String(1000))
    
    def __repr__(self):
        return "<Dy(name = '%s',link = '%s')>" % (self.name,self.link)
    
