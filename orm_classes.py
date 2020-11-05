from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy import select, func, and_, or_, between, union
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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



    def getName(self):
        return "Wonderful "+self.name

    def getPopulation(self):
        return self.population


Base.metadata.create_all(engine)

Kyiv = City(id =1, name = "Kyiv", population = 3700000)

session = sessionmaker(engine)
open_session = session()

#add info to table

# open_session.add_all([
#     # City( name = "Kyiv", population = 3700000),
#     # City( name = "Kharkiv", population = 1400000)
#     City( name = "Lviv", population = 721000)
# ])
open_session.commit()

# print(Kyiv.getName())
# print(Kyiv.getPopulation())

#select all cities with their populations

cities = open_session.query(City).all()
for city in cities:
    print(city.getName(), "population is ", city.getPopulation())

#select first element of table

first_city = open_session.query(City).first()
print(first_city.name, "is first city on DB")

city_id = open_session.query(City).get(6)
print("Second city on DB is ", city_id.name)


#update info (содержит ошибки)

# lviv = open_session.query(City).get(7)
# lviv.population = lviv.getPopulation()+20000
#
# open_session.commit()
#
# for lviv in open_session.query(City).all():
#     lviv.population = lviv.getPopulation()+20000
#
# open_session.commit()

#select with filter

cities = open_session.query(City).filter(and_(City.population>1000000, City.population<2000000))
for city in cities:
    print(city.population)


#delete info from table

# open_session.query(City).filter(and_(City.population>3000000)).delete()

