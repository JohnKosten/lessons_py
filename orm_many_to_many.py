from sqlalchemy import create_engine, Column, String, Integer, and_, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)
Base = declarative_base()

class Train(Base):
    __tablename__ = "train"

    id = Column(Integer, primary_key=True)
    name = Column(String(10))

    passenger = relationship('Passenger',secondary = 'stations')


class Passenger(Base):
    __tablename__ = "passenger"

    id = Column(Integer, primary_key=True)
    name = Column(String(10))

    train = relationship('Train',secondary = 'stations')

class Station(Base):
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True)
    passenger_id = Column(Integer, ForeignKey("passenger.id"))
    train_id = Column(Integer, ForeignKey("train.id"))

Base.metadata.create_all(engine)

session = sessionmaker(engine)
open_session = session()

passenger1 =Passenger(name = 'Igor')
passenger2 =Passenger(name = 'Svetlana')


train1 = Train(name='Intercity')
train2 = Train(name='Old')

# train1.passenger.append(passenger1)
# train2.passenger.append(passenger1)
# train2.passenger.append(passenger2)

# passenger1.train.append(train1)
# passenger1.train.append(train2)
# passenger2.train.append(train2)


session = sessionmaker(engine)
open_session = session()
# open_session.add(train1)
# open_session.add(train2)
# open_session.add(passenger1)
# open_session.add(passenger2)

open_session.commit()


Igor  = open_session.query(Passenger).get(7)
train = open_session.query(Train).get(7)
if Igor:
    print(Igor.name)
    Igor.train.append(train1)
    for train in Igor.train:
        print(train.name)

open_session.commit()

