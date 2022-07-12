from bottle import route, run, template, request, response, post, get, delete, put, static_file
import os
import sqlite3     

db = sqlite3.connect('forumdata.db')
cur = db.cursor()

abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
abs_views_path = os.path.join(abs_app_dir_path, 'views')

@route('/<filename>.css')
def stylesheets(filename):
    return static_file('{}.css'.format(filename), root='static')

@route('/')
@route('/threadlist')
@route('/index')
def index():
    return template('index.tpl')

@route('/login')
def login():
    return template('login.tpl')

@route('/login', method='POST') 
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    statement = f"SELECT username from users WHERE username='{username}' AND Password = '{password}';"
    cur.execute(statement)
    if not cur.fetchone():
        return "<p>Your log in attempt has failed</p>"
    else:
        return "<p>You have logged in successfuly</p>"

@route('/signup')
def signup():
    return template('signup.tpl')

@route('/signup', method='POST') 
def do_signup():
    username = request.forms.get('username')
    password = request.forms.get('password')
    confirm_password = request.forms.get('confirm password')
    first_name = request.forms.get('first name')
    last_name = request.forms.get('last_name')
    email = request.forms.get('email address')
    if password != confirm_password:
        return "<p>Password not the same</p>"
    statement = f"INSERT INTO Users (Username, Password, First_Name, Last_Name, Email_Address) VALUES (?,?,?,?,?)';"
    data_tuple = (username, password, first_name, last_name, email)
    cur.execute(statement, data_tuple)

run(host='localhost', port=8080, debug=True)
