from utils.utils_db import *

sql_create_db: str = f'''
        CREATE TABLE {TABLE_NAME}
        ({CONTACT_NAME_COLUMN} varchar(255), {PHONE_COLUMN} varchar(128) UNIQUE)
        '''

sql_change(sql_create_db)
