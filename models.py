#!/usr/bin/env python
# encoding: utf-8


from peewee import *
database = MySQLDatabase('simpledict', user='root', password='likeyiyymac', charset='utf8mb4')


class BaseModel(Model):
    class Meta:
        database = database


class Word(BaseModel):
    word = CharField(null=True, unique=True)
    count = IntegerField(default=0)
    trans = CharField(null=True)
