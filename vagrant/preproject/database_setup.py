## CONFIGURATION CODE ##
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()





## CLASS CONFIGURATION ##

class Catalog(Base):
    ## TABLE ##
    __tablename__ = 'catalog'

    ## ATTRIBUTES ##
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)


class CatalogItem(Base):
    ## TABLE ##
    __tablename__ = 'catalog_item'

    ## ATTRIBUTES ##
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(1000))

    catalog_id = Column(Integer, ForeignKey('catalog.id'))
    catalog = relationship(Catalog)








## CONFIGURATION CODE ##
engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
