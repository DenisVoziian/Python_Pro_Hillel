import sqlite3

DATABASE_NAME: str = 'users.db'
TABLE_NAME: str = 'phones'
CONTACT_NAME_COLUMN: str = "contactName"
PHONE_COLUMN: str = "phone"


def sql_change(sql_script: str) -> None:
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        cur.execute(sql_script)
        conn.commit()
    finally:
        conn.close()


def sql_read(sql_script: str) -> list:
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        cur.execute(sql_script)
        data_db: list = cur.fetchall()
    finally:
        conn.close()

    return data_db
