from peewee import (Model, CharField, SqliteDatabase, IntegrityError, TextField, IntegerField)

DATABASE = SqliteDatabase("nyumba.db")


class House(Model):
    plot_no = CharField(max_length=200, unique=True)
    no_rooms = IntegerField()
    rent = IntegerField()
    no_bathrooms = IntegerField()
    location = TextField()
    nearby_amenities = TextField()
    rating = IntegerField()

    class Meta:
        database = DATABASE