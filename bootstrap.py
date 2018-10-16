from models.house import House
from models.agent import Agent
from peewee import SqliteDatabase, IntegrityError

DATABASE = SqliteDatabase("nyumba.db")


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([House, Agent], safe=True)
    try:
        House.create(
            plot_no="kawang_34",
            no_rooms=5,
            rent=20000,
            no_bathrooms=2,
            location="Kawangware, Nairobi",
            nearby_amenities="Kawangware Primary",
            rating=5
        )
        House.create(
            plot_no="kawang_35",
            no_rooms=4,
            rent=15000,
            no_bathrooms=1,
            location="Kawangware, Nairobi",
            nearby_amenities="Kawangware Group of schools",
            rating=5
        )
    except IntegrityError:
        pass
      
    try:
        Agent.create(
              name="john doe",
              business_number="0712345678",
              email="johndoe@gmail.com",
                
        )
    except IntegrityError:
        pass

    DATABASE.close()