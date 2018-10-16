from peewee import (Model, CharField, SqliteDatabase, IntegrityError, TextField, IntegerField)

DATABASE = SqliteDatabase("nyumba.db")


class Agent(Model):
    name = CharField(max_length=100, unique=True)
    business_number = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)

    class Meta:
        database = DATABASE