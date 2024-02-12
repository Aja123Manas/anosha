import sqlite3

conn = sqlite3.connect('afternoon.db')
print("opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1,'FAITH KARIMI',34, 340000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'TATIANA NYOKABI',32, 120000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'DENG HAKIM',27, 85000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'DAVID NJOROGE',41, 560000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'ASUNTA HASSAN',23, 300000.00)")

conn.commit()
print("Employee inserted successfully")
conn.close()
