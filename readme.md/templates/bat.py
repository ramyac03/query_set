from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

engine =create_engine("mysql+pymysql://root:root@localhost/implenet",echo = True)
meta =MetaData()
rate =Table(
    'rate',meta,
    Column('id', Integer,primary_key =True),
    Column('name',String (17)),
    Column('lastname',String(23))
)
meta.create_all(engine)