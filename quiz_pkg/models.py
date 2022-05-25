from peewee import *

db = SqliteDatabase('quiz_app.db')


class User(Model):
    username = CharField()
    password = CharField()
    name = CharField()

    class Meta:
        database = db


class Category(Model):
    name = CharField()

    class Meta:
        database = db


class Question(Model):
    category = ForeignKeyField(Category, backref="categories")
    question = CharField()
    code = TextField(null=True)

    class Meta:
        database = db


class Answer(Model):
    question = ForeignKeyField(Question, backref="questions")
    text = CharField()
    is_correct = BooleanField()

    class Meta:
        database = db
