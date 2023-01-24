from basecreate import engine, rose
from sqlalchemy.orm import sessionmaker

session =sessionmaker(bind =engine ) #session maker is bound to object(engine)
session =session()# set up the session
c1 =rose(name='ram',adress='xyz',email ='eample')
#session.add(c1)# adding the object
session.add_all([ #adding all elements
    rose(name = 'Komal Pande', adress = 'Koti, Hyderabad', email = 'komal@gmail.com'), 
   rose(name = 'Rajender Nath', adress = 'Sector 40, Gurgaon', email = 'nath@gmail.com'), 
   rose(name = 'S.M.Krishna', adress = 'Budhwar Peth, Pune', email = 'smk@gmail.com')

])
session.commit()#pending transactions
