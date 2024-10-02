import enum
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
# try:
#     result = render_er(Base, 'diagram.png')
#     print("Success! Check the diagram.png file")
# except Exception as e:
#     print("There was a problem genering the diagram")
#     raise e

class MyEnum(enum.Enum):
    video = 1
    imagen = 2
    historias = 3
    post = 4

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    
    def to_dict(self):
        return {}

class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    eyeColor = Column(String(100), nullable=False)
    birthDate = Column(String(100), nullable=False)
    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    size = Column(String(100), nullable=False)
    climate = Column(String(100), nullable=False)
    
    def to_dict(self):
        return {}

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(String(100), nullable=False)
    length = Column(String(100), nullable=False)
    cargoCapacity = Column(String(100), nullable=False)
    def to_dict(self):
        return {}

class Favorites(Base):
    __tablename__ = 'Favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    planet_id = Column(Integer, ForeignKey('Planets.id'))
    character_id = Column(Integer, ForeignKey('Character.id'))
    vehicles_id = Column(Integer, ForeignKey('Vehicles.id'))
    User = relationship(User)
    planets = relationship(Planets)
    character = relationship(Character)
    vehicles = relationship(Vehicles) 
    def to_dict(self):
        return {}

# ## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e