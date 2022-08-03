from flask import Flask, request
from utils import utils_db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello User!'


@app.route('/emails/create/')
def email_create():
    email = request.args['email']
    name = request.args['name']

    sql_script = f'''
            INSERT INTO users
            VALUES ('{name}', '{email}');
            '''

    utils_db.sql_change(sql_script)

    return 'Emails created'


@app.route('/emails/read/')
def email_read():
    sql_script = f'''
            SELECT * FROM users;
            '''

    emails = utils_db.sql_read(sql_script)
    return str(emails)


@app.route('/emails/delete/')
def email_delete():
    email = request.args['email']
    sql_script = f'''
            DELETE FROM users WHERE Email == '{email}';
            '''
    utils_db.sql_change(sql_script)

    return 'Email delete'


@app.route('/emails/update/')
def email_update():
    email = request.args['email']
    name = request.args['name']

    sql_script = f'''
            UPDATE users 
            SET UserName = '{name}'
            WHERE Email == '{email}';
            '''

    utils_db.sql_change(sql_script)

    return 'Email update'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
