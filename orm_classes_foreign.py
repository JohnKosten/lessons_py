from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy import select, func, and_, or_, between, union
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo = False)

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


Base.metadata.create_all(engine)

session = sessionmaker(engine)
open_session = session()

Kyiv = City(name="Kyiv", population=3740000)
Kyiv.places = [ Places(name="Dnipro"), Places(name="Maidan"), Places(name="Gidropark")]

open_session.add(Kyiv)
open_session.commit()
