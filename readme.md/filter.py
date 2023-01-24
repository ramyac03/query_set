from basecreate import rose,engine
from sqlalchemy import and_,or_
from sqlalchemy.orm import sessionmaker
session=sessionmaker(bind=engine)
session=session()
#result =session.query(rose).filter(rose.id>2)
#result =session.query(rose).filter(rose.id==2) ---equal operator
#result =session.query(rose).filter(rose.id!=2) --not equal operator
#result =session.query(rose).filter(rose.name.like('Ra%'))
#result =session.query(rose).filter(rose.id.in_([1,3]))
result =session.query(rose).filter(and_(rose.id>2,rose.name.like('Ra%')))
result =session.query(rose).filter(or_(rose.id>4,rose.name.like('Ra5')))
for row in result:
 print( "id:",row.id,"name:",row.name ,"adress:",row.adress)