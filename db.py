from peewee import *
import datetime
import json


db = MySQLDatabase(
    'wordnet',  # Required by Peewee.
    user='root',  # Will be passed directly to psycopg2.
    password='z',
    host='127.0.0.1',
)



class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = db


    def __str__(self):
        r = {}
        for k in self._data.keys():
          try:
             r[k] = str(getattr(self, k))
          except:
             r[k] = json.dumps(getattr(self, k))
        return str(r)



class Word(BaseModel):
    class Meta:
        db_table = 'word'

    lex_form = TextField(unique=True)
    lex_form_latin = TextField(unique=True)
    description = TextField()
    giperonim = TextField()
    giperonim_latin = TextField()
    giponim = TextField()
    giponim_latin = TextField()
    holonim = TextField()
    holonim_latin = TextField()
    meronim = TextField()
    meronim_latin = TextField()
    sinonim = TextField()
    sinonim_latin = TextField()
    ontonim = TextField()
    ontonim_latin = TextField()
    omonim = TextField()
    omonim_latin = TextField()
    xml = TextField()



