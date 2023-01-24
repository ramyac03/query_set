from basecreate import rose,engine
from sqlalchemy.orm import sessionmaker
session=sessionmaker(bind=engine)
session=session()
result=session.query(rose).get(2)
print( "id:",result.id,"name:",result.name ,"adress:",result.adress)
result.name="ram"
session.commit()