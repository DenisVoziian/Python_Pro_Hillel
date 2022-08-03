from flask import Flask, request
from utils import utils_db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello User!'


@app.route('/phones/create/')
def phones_create():
    phone = request.args['phone']
    contact_name = request.args['contactName']

    sql_script = f'''
            INSERT INTO phones
            VALUES ('{contact_name}', '{phone}');
            '''

    utils_db.sql_change(sql_script)

    return 'Phone created'


@app.route('/phones/read/')
def phones_read():
    sql_script = f'''
            SELECT * FROM phones;
            '''

    phones = utils_db.sql_read(sql_script)
    return str(phones)


@app.route('/phones/delete/')
def email_delete():
    phone = request.args['phone']
    sql_script = f'''
            DELETE FROM phones WHERE phone == '{phone}';
            '''
    utils_db.sql_change(sql_script)

    return 'Phone delete'


@app.route('/phones/update/')
def phone_update():
    phone = request.args['phone']
    contact_name = request.args['contactName']

    sql_script = f'''
            UPDATE phones 
            SET contactName = '{contact_name}'
            WHERE phone == '{phone}';
            '''

    utils_db.sql_change(sql_script)

    return 'Name update by phone number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
