import sqlite3

DATABASE_NAME = 'users.db'
TABLE_NAME = 'phones'
CONTACT_NAME_COLUMN = "contactName"
PHONE_COLUMN = "phone"


def sql_change(sql_script):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        cur.execute(sql_script)
        conn.commit()
    finally:
        conn.close()


def sql_read(sql_script):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        cur.execute(sql_script)
        data_db = cur.fetchall()
    finally:
        conn.close()

    return data_db
