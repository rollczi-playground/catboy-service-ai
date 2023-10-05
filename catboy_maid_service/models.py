## models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    location = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    services = relationship('Service', backref='restaurant')

    def __init__(self, id: int, name: str, location: str, type: str):
        self.id = id
        self.name = name
        self.location = location
        self.type = type

    def add_service(self, service):
        self.services.append(service)


class Service(db.Model):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    description = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    catboys = relationship('Catboy', backref='service')

    def __init__(self, id: int, description: str, price: float):
        self.id = id
        self.description = description
        self.price = price


class Catboy(db.Model):
    __tablename__ = 'catboys'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    costume = Column(String(50), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'))

    def __init__(self, id: int, name: str, age: int, costume: str):
        self.id = id
        self.name = name
        self.age = age
        self.costume = costume

# Create the database tables
db.create_all()
