from bat import engine, rate

ins=rate.insert().values (name='ram',lastname='nithi')#insert method (students =object which we created,insert =method)
conn= engine.connect()#connect to object which we created and connect to db
#result=conn.execute(ins) -using execute method ,and insert one values
result=conn.execute(rate.insert(),[ 
    {'name':'Rajiv', 'lastname' : 'Khanna'},
   {'name':'Komal','lastname' : 'Bhandari'},
   {'name':'Abdul','lastname' : 'Sattar'}, #insert using many values with many()method
])