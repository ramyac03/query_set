from bat import rate,engine
s =rate.select().where (rate.c.id>1)#select method
conn =engine.connect()
result =conn.execute(s)
row =result.fetchone() #fetching the row
for row in result:# using loop for print the result in new line
 print(row)