import sqlite3 

con = sqlite3.connect("database")

cur = con.cursor()

cur.execute("CREATE TABLE stock (type VARCHAR(10), color VARCHAR(10), box INT, units ) ")

con.close()