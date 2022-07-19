from bottle import route, run, template, request
from bottle import response, post, get, delete, put, view, redirect, response, static_file
import uuid
import os
import sqlite3

sessions = {}

db = sqlite3.connect('forumdata.db')
cur = db.cursor()

abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
abs_views_path = os.path.join(abs_app_dir_path, 'views')

@route('/')
@route('/threadlist')
@view('/')
def index():
    #statement = f"SELECT threadnumber, title, creator, datemade, score from threadlist LIMIT 20;"
    #cur.execute(statement)
    #DATABASE TO VARIABLES FOR THREADLIST
    user_session_id = request.get_cookie("user_session_id")
    if not user_session_id or user_session_id not in sessions:
        return template("index.tpl", user="Guest")
    else:
        user = sessions[user_session_id]
        return template("index.tpl", user=user)

@route('/threadlist/page/<pagenumber>')
@view('/page/<pagenumber>')
def index(pagenumber):
    #statement = f"SELECT threadnumber, title, creator, datemade, score from threadlist LIMIT 20 OFFSET " + ((pagenumber+1)*20) + ";"
    #cur.execute(statement)
    #DATABASE TO VARIABLES FOR THREADLIST
    user_session_id = request.get_cookie("user_session_id")
    if not user_session_id or user_session_id not in sessions:
        return template("index.tpl", user="Guest")
    else:
        user = sessions[user_session_id]
        return template("index.tpl", user=user)

@route('/login')
def login():
    user_session_id = request.get_cookie("user_session_id")
    if not user_session_id or user_session_id not in sessions:
        user="Guest"
    else:
        user = sessions[user_session_id]
    return template('Login.tpl', LogInFailed=False, Registration_Success=False, user=user)

@route('/login', method='POST') 
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    statement = f"SELECT username from users WHERE username='{username}' AND Password = '{password}';"
    cur.execute(statement)
    if not cur.fetchone():
        return template("Login.tpl", LogInFailed=True, Registration_Success=False)
    user_session_id = str(uuid.uuid4())
    statement = f"SELECT Username, First_Name, Last_Name, Email_Address, Registered_Date, isAdmin FROM Users Where Username = '{username}'"
    cur.execute(statement)
    sessions[user_session_id] = cur.fetchall()
    response.set_cookie("user_session_id", user_session_id)
    return redirect('/')

@route('/signup')
def signup():
    user_session_id = request.get_cookie("user_session_id")
    if not user_session_id or user_session_id not in sessions:
        user="Guest"
    else:
        user = sessions[user_session_id]
    return template('Signup.tpl', Email_Taken=False, Username_Taken=False, Not_Same_Password=False, user=user)

@route('/signup', method='POST') 
def do_signup():
    username = request.forms.get('username')
    password = request.forms.get('password')
    confirm_password = request.forms.get('confirm-password')
    first_name = request.forms.get('first-name')
    last_name = request.forms.get('last-name')
    email = request.forms.get('email-address')
    if password != confirm_password:
        return template('Signup.tpl', Username_Taken=False, Email_Taken=False, Not_Same_Password=True)
    print(username)
    statement = f"SELECT Username FROM Users WHERE Username = '{username}'"
    cur.execute(statement)
    if cur.fetchone() is not None:
        return template('Signup.tpl', Username_Taken=True, Email_Taken=False, Not_Same_Password=False)
    statement = f"SELECT Email_Address FROM Users WHERE Email_Address = '{email}'"
    cur.execute(statement)
    if cur.fetchone() is not None:
        return template('Signup.tpl', Email_Taken=True, Username_Taken=False, Not_Same_Password=False)
    statement = "INSERT INTO Users (Username, Password, First_Name, Last_Name, Email_Address, Registered_Date) VALUES (?,?,?,?,?, date('now'));"
    data_tuple = (username, password, first_name, last_name, email)
    cur.execute(statement, data_tuple)
    db.commit()
    return template('login.tpl', Registration_Success=True, LogInFailed=False)
    
@route('/threadpage/<threadnumber>')
def threadpage(threadnumber):
    #statement = f"SELECT commentnumber, datemade, content, score from commentlist WHERE thread='threadnumber' LIMIT 20"
    #cur.execute(statement)
    #DATABASE TO VARIABLES FOR COMMENT LIST
    user_session_id = request.get_cookie("user_session_id")
    if not user_session_id or user_session_id not in sessions:
        return template("threadpage.tpl", user="Guest")
    else:
        user = sessions[user_session_id]
        return template("threadpage.tpl", user=user)
    return template('threadpage.tpl')
    
@route('/threadpage/<threadnumber>/page/<pagenumber>')
def threadpage(threadnumber, pagenumber):
    #statement = f"SELECT commentnumber, datemade, content, score from commentlist WHERE thread='threadnumber' LIMIT 20 OFFSET " + ((pagenumber+1)*20) + ";"
    #cur.execute(statement)
    #DATABASE TO VARIABLES FOR COMMENT LIST
    user_session_id = request.get_cookie("user_session_id")
    if not user_session_id or user_session_id not in sessions:
        return template("threadpage.tpl", user="Guest")
    else:
        user = sessions[user_session_id]
        return template("threadpage.tpl", user=user)
    return template('threadpage.tpl')
    
@route('/useraccount')
def useraccount():
    #statement = f"SELECT Username, Password, First_Name, Last_Name, Email_Address  from Users WHERE Username='username'"
    #cur.execute(statement)
    #DATABASE TO VARIABLES FOR PREFILL USER ACCOUNT DETAILS
    user_session_id = request.get_cookie("user_session_id")
    if not user_session_id or user_session_id not in sessions:
        return template("useraccount.tpl", user="Guest", Email_Taken=False, Username_Taken=False, Not_Same_Password=False)
    else:
        user = sessions[user_session_id]
        return template("useraccount.tpl", user=user, Email_Taken=False, Username_Taken=False, Not_Same_Password=False)
        
@route('/saved')
def saved():
    #statement = f"SELECT threadnumber, title, creator, datemade, score from savedthreads JOIN threadlist ON savedthreads.threadnumber=threadlist.threadnumber WHERE savedthreads.username = currentuser LIMIT 20"
    #cur.execute(statement)
    #DATABASE TO VARIABLES FOR THREADLIST
    user_session_id = request.get_cookie("user_session_id")
    if not user_session_id or user_session_id not in sessions:
        return template("saved.tpl", user="Guest")
    else:
        user = sessions[user_session_id]
        return template("saved.tpl", user=user)
        
@route('/saved/<pagenumber>')
def savedpage(pagenumber):
    #statement = f"SELECT threadnumber, title, creator, datemade, score from savedthreads JOIN threadlist ON savedthreads.threadnumber=threadlist.threadnumber WHERE savedthreads.username = currentuser LIMIT 20 OFFSET " + ((pagenumber+1)*20) + ";"
    #cur.execute(statement)
    #DATABASE TO VARIABLES FOR THREADLIST
    user_session_id = request.get_cookie("user_session_id")
    if not user_session_id or user_session_id not in sessions:
        return template("saved.tpl", user="Guest")
    else:
        user = sessions[user_session_id]
        return template("saved.tpl", user=user)
        
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

run(host='localhost', port=8080, debug=True, reloader=True)
