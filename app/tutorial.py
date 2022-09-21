import sqlite3
import json

con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS cars(id integer primary key, year, model)")
cur.execute(
    "INSERT INTO cars VALUES (3, '2020','Mazda 3'),(4, '2021','Ford focus')")
con.commit()
c = cur.execute("select * from cars")
print("ff")
