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



# class Monitor(BaseModel):
#     class Meta:
#         db_table = 'Monitors'
#
#     name = CharField(max_length=64, db_column = "Name")





# class Event(BaseModel):
#     class Meta:
#         db_table = 'Events'
#
#     monitor_id = IntegerField(db_column = "MonitorId")
#     cause = CharField(db_column = "Cause")
#     length = DecimalField(db_column = "Length")
#     start_time = DateTimeField(db_column = "StartTime")






# class PrVideo(BaseModel):
#     class Meta:
#         db_table = 'word'
#
#     path_and_file = CharField(unique=True, max_length=500)
#     start_time = DateTimeField()
#     length = DecimalField()
#     created_at = DateTimeField(default=datetime.datetime.now)



class Word(BaseModel):
    class Meta:
        db_table = 'word'

    lex_form = TextField(unique=True)
    lex_form_latin = TextField(unique=True)
    giperonim = TextField()
    giperonim_latin = TextField()
    giponim = TextField()
    giponim_latin = TextField()
    meronim = TextField()
    meronim_latin = TextField()
    sinonim = TextField()
    sinonim_latin = TextField()
    ontonim = TextField()
    ontonim_latin = TextField()
    omonim = TextField()
    omonim_latin = TextField()





# class PrLog(BaseModel):
#     notes = CharField(max_length=1000)
#     created_at = DateTimeField(default=datetime.datetime.now)





# if not PrVideo.table_exists():
#     db.create_tables([PrVideo])
#
# if not PrLog.table_exists():
#     db.create_tables([PrLog])