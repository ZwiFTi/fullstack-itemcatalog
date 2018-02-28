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

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class CatalogItem(Base):
    ## TABLE ##
    __tablename__ = 'catalog_item'

    ## ATTRIBUTES ##
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(1000))

    catalog_id = Column(Integer, ForeignKey('catalog.id'))
    catalog = relationship(Catalog)

    user = Column(String(80), nullable = False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'catalog': self.catalog.name,
        }








## CONFIGURATION CODE ##
engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
