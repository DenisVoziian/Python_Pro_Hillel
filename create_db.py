import sqlite3

conn = sqlite3.connect('users.db')

cur = conn.cursor()

cur.execute('''
    CREATE TABLE users
    (UserName varchar(255), Email varchar(128) UNIQUE)
    ''')

conn.commit()
conn.close()
