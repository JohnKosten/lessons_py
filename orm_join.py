from sqlalchemy import create_engine, Column, String, Integer, and_, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=False)
Base = declarative_base()

class City(Base):

    __tablename__= "city"

    #id
    id = Column(Integer, primary_key=True)
    # name
    name = Column(String(10))
    # age
    population = Column(Integer)
    #link to places
    places = relationship("Places", back_populates="city")

    def getName(self):
        return "Wonderful "+self.name

    def getPopulation(self):
        return self.population

class Places(Base):

    __tablename__= "places"

    # id
    id = Column(Integer, primary_key=True)
    # name
    name = Column(String(10))
    # fk
    city_fk = Column(Integer, ForeignKey('city.id'))
    #link to cities
    city = relationship("City", back_populates = "places")


session = sessionmaker(engine)
open_session = session()

result1= open_session.query(City,Places).filter(City.id == Places.city_fk).all()
for city, places in result1:
    print(city.name, places.name)

# VS

result2 = open_session.query(City).join(Places).all()
for city in result2:
    print(city.name)
    for places in city.places:
        print(places.name)