from bat import rate,engine
s =rate.select()#select method
conn =engine.connect()
result =conn.execute(s)
row =result.fetchone() #fetching the row
for row in result:# using loop for print the result in new line
 print(row)