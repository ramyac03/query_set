from bat import engine,rate
conn=engine.connect()
stmt=rate.delete().where(rate.c.lastname=='sattar')
conn.execute(stmt)
s=rate.select()
conn.execute(s).fetchall()