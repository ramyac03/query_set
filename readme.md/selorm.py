from basecreate import engine ,rose
from sqlalchemy.orm import sessionmaker
session =sessionmaker(bind=engine)
session =session()

result =session.query(rose).filter(rose.id>1)
#for row in result:
 #  print ("ID:", row.id, "Name: ",row.name, "Adress:",row.adress)
list=[] #create list
for row in result: #using for loop
   dict ={
    "name": row.name,
    "adress": row.adress,
    "email": row.email
   }
   list.append(dict)

print(list)
print(list)
