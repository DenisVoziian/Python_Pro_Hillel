from flask import Flask, request
from utils.utils_db import *

app = Flask(__name__)


@app.route('/')
def hello_page():
    return 'Hello User!'


@app.route('/phones/create/')
def phones_create():
    phone = request.args['phone']
    contact_name = request.args['contactName']
    sql_script = f'''
            INSERT INTO {TABLE_NAME}
            VALUES ('{contact_name}', '{phone}');
            '''

    sql_change(sql_script)

    return 'Phone created'


@app.route('/phones/read/')
def phones_read():
    sql_script = f'''
            SELECT * FROM {TABLE_NAME};
            '''

    phones = sql_read(sql_script)

    return str(phones)


@app.route('/phones/update/')
def phones_update():
    phone = request.args['phone']
    contact_name = request.args['contactName']
    sql_script = f'''
            UPDATE {TABLE_NAME} 
            SET {CONTACT_NAME_COLUMN} = '{contact_name}'
            WHERE {PHONE_COLUMN} == '{phone}';
            '''

    sql_change(sql_script)

    return 'Name update by phone number'


@app.route('/phones/delete/')
def phones_delete():
    phone = request.args['phone']
    sql_script = f'''
            DELETE FROM {TABLE_NAME} WHERE {PHONE_COLUMN} == '{phone}';
            '''

    sql_change(sql_script)

    return 'Phone delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
