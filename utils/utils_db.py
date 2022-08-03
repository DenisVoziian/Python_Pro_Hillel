import sqlite3


def sql_change(sql_script):
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute(sql_script)
        conn.commit()
    finally:
        conn.close()


def sql_read(sql_script):
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute(sql_script)
        data_db = cur.fetchall()
    finally:
        conn.close()

    return data_db