from utils import utils_db

sql_create_db = '''
    CREATE TABLE phones
    (contactName varchar(255), phone varchar(128) UNIQUE)
    '''

utils_db.sql_change(sql_create_db)
