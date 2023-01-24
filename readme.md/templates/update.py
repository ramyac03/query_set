from bat import rate,engine
conn=engine.connect()
stmt=rate.update().where(rate.c.lastname=='khanna').values(lastname='ram')
conn.execute(stmt)
s=rate.select()
conn.execute(s).fetchall()