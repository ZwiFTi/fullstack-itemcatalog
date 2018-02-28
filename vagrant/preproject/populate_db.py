from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catalog, CatalogItem

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

myFirstCatalog = Catalog(name = "Snowboarding")
session.add(myFirstCatalog)
session.commit()

myFirstCatalog2 = Catalog(name = "Skiing")
session.add(myFirstCatalog2)
session.commit()

myFirstCatalog3 = Catalog(name = "Mountainbiking")
session.add(myFirstCatalog3)
session.commit()

myFirstCatalog4 = Catalog(name = "Rafting")
session.add(myFirstCatalog4)
session.commit()

myFirstCatalog5 = Catalog(name = "DrinkingBeer")
session.add(myFirstCatalog5)
session.commit()
