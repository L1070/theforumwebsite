from bottle import route, run, template, request, SimpleTemplate
from bottle import response, post, get, delete, put, view, redirect, response, static_file
import uuid
import os, json
import sqlite3

sessions = {}

db = sqlite3.connect('forumdata.db')
cur = db.cursor()

abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
abs_views_path = os.path.join(abs_app_dir_path, 'views')


def Cookie_Setting():
    user_session_id = request.get_cookie("user_session_id")
    if not user_session_id or user_session_id not in sessions:
        return "Guest"
    else:
        user = sessions[user_session_id]
        return user

@route('/')
@route('/threadlist')
@route('/0')
@view('/')
def index():
    statement = "SELECT Thread_ID, Title_Name, Username, Date_Made, Score from Thread WHERE isPinned = 1;"
    cur.execute(statement)
    PinnedThreads = cur.fetchall()
    statement = "SELECT Thread_ID, Title_Name, Username, Date_Made, Score from Thread WHERE isPinned = 0 LIMIT 20;"
    cur.execute(statement)
    UnPinnedThreads = cur.fetchall()
    #DATABASE TO VARIABLES FOR THREADLIST ----- Not displaying anything...
    user = Cookie_Setting()
    return template("index.tpl", user=user, PinnedThreads=PinnedThreads, UnPinnedThreads=UnPinnedThreads, offset_num=0)

@route('/threadlist/page/<pagenumber>')
@route('/page/<pagenumber>')
@route('/<pagenumber>')
@view('/page/<pagenumber>')
def index(pagenumber):
    pagenumber = int(pagenumber)
    offset_num = (pagenumber + 1) * 20
    statement = f"SELECT Thread_ID, Title_Name, Username, Body_Text Date_Made, Score from Thread WHERE isPinned = 0 LIMIT 20 OFFSET {offset_num};"
    cur.execute(statement)
    UnPinnedThreads = cur.fetchall()
    #DATABASE TO VARIABLES FOR THREADLIST ------ Done, but not testing for displaying yet
    user = Cookie_Setting()
    return template("index.tpl", user=user, PinnedThreads="", UnPinnedThreads=UnPinnedThreads, offset_num=offset_num)

@route('/login')
def login():
    user = Cookie_Setting()
    return template('Login.tpl', LogInFailed=False, Registration_Success=False, user=user)

@route('/login', method='POST') 
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    statement = f"SELECT username from users WHERE username='{username}' AND Password = '{password}';"
    cur.execute(statement)
    if not cur.fetchone():
        user = Cookie_Setting()
        return template("Login.tpl", LogInFailed=True, Registration_Success=False, user=user)
    user_session_id = str(uuid.uuid4())
    statement = f"SELECT Username, First_Name, Last_Name, Email_Address, Registered_Date, isAdmin FROM Users Where Username = '{username}'"
    cur.execute(statement)
    sessions[user_session_id] = cur.fetchall()
    response.set_cookie("user_session_id", user_session_id)
    return redirect('/')

@route('/logout', method="GET")
def do_logout():
    user_session_id = request.get_cookie("user_session_id")
    if user_session_id or user_session_id in sessions:
        sessions.pop(user_session_id)
    return redirect('/')

@route('/signup')
def signup():
    user = Cookie_Setting()
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
@route('/threadpage/<threadnumber>/0')
def threadpage(threadnumber):
#    statement = f"SELECT Comment_ID, Date_Created, Body_Text, Score from Comment WHERE Thread_ID = '{threadnumber}' AND isPinned = 1;"
    statement = "SELECT Thread_ID, Title_Name, Username, Date_Made, Score from Thread WHERE isPinned = 1;"
    cur.execute(statement)
    PinnedComments = cur.fetchall()
#    statement = f"SELECT Comment_ID, Date_Created, Body_Text, Score from Comment WHERE Thread_ID = '{threadnumber}' AND isPinned = 0 LIMIT 20;"
    statement = "SELECT Thread_ID, Title_Name, Username, Date_Made, Score from Thread WHERE isPinned = 0 LIMIT 20;"
    cur.execute(statement)
    UnPinnedComments = cur.fetchall()
    #DATABASE TO VARIABLES FOR COMMENT LIST -- done but not testing yet for displaying
    user = Cookie_Setting()
    return template("threadpage.tpl", user=user, PinnedComments=PinnedComments, UnPinnedComments=UnPinnedComments, threadnumber=threadnumber)
    
@route('/threadpage/<threadnumber>/page/<pagenumber>')
def threadpage(threadnumber, pagenumber):
    pagenumber = int(pagenumber)
    offset_num = (pagenumber + 1) * 20
    statement = f"SELECT Comment_ID, Date_Created, Body_Text, Score from Comment WHERE Thread_ID = '{threadnumber}' LIMIT 20 OFFSET {offset_num};"
    cur.execute(statement)
    Comments = cur.fetchall()
    #DATABASE TO VARIABLES FOR COMMENT LIST -- done but not testing yet for displaying
    user = Cookie_Setting()
    return template("threadpage.tpl", user=user, Comments=Comments)
    
@route('/useraccount')
def useraccount():
    user_session_id = request.get_cookie("user_session_id")
    user = sessions[user_session_id]
    username = user[0][0]
    statement = f"SELECT Username, Password, First_Name, Last_Name, Email_Address from Users WHERE Username='{username}';"
    cur.execute(statement)
    stored_info = cur.fetchall()
    #DATABASE TO VARIABLES FOR PREFILL USER ACCOUNT DETAILS -- done but not testing yet for displaying
    return template("useraccount.tpl", user=user, stored_info=stored_info, Email_Taken=False, Username_Taken=False, Not_Same_Password=False)

@route('/useraccount', method='POST')
def do_changeaccount():
    username = request.forms.get('username')
    password = request.forms.get('password')
    confirm_password = request.forms.get('confirm-password')
    first_name = request.forms.get('first-name')
    last_name = request.forms.get('last-name')
    email = request.forms.get('email-address')
    if password != confirm_password:
        user = Cookie_Setting()
        return template('useraccount.tpl', Username_Taken=False, Email_Taken=False, Not_Same_Password=True, user=user)
    print(username)
    statement = f"SELECT Username FROM Users WHERE Username = '{username}'"
    cur.execute(statement)
    if cur.fetchone() is not None:
        user = Cookie_Setting()
        return template('useraccount.tpl', Username_Taken=True, Email_Taken=False, Not_Same_Password=False, user=user)
    statement = f"SELECT Email_Address FROM Users WHERE Email_Address = '{email}'"
    cur.execute(statement)
    if cur.fetchone() is not None:
        user = Cookie_Setting()
        return template('useraccount.tpl', Email_Taken=True, Username_Taken=False, Not_Same_Password=False)
    statement = "INSERT INTO Users (Username, Password, First_Name, Last_Name, Email_Address, Registered_Date) VALUES (?,?,?,?,?, date('now'));"
    data_tuple = (username, password, first_name, last_name, email)
    cur.execute(statement, data_tuple)
    db.commit()
    user = Cookie_Setting()
    return template('login.tpl', Registration_Success=True, LogInFailed=False, user=user)

@route('/saved')
@route('/saved/0')
def saved():
    user = Cookie_Setting()
    username = user[0][0]
    statement = f"SELECT COUNT(*) from Thread WHERE Username = '{username}' LIMIT 20;"
    cur.execute(statement)
    count = cur.fetchall()
    statement = f"SELECT Thread_ID, Title_Name, Username, Date_Made, Score from Thread WHERE Username = '{username}' LIMIT 20;"
    cur.execute(statement)
    Saved_Threads = cur.fetchall()
    #DATABASE TO VARIABLES FOR THREADLIST -- done but not testing yet for displaying
    return template("saved.tpl", user=user, Saved_Threads=Saved_Threads, count=count, offset_num=0)
        
@route('/saved/<pagenumber>')
def savedpage(pagenumber):
    user = Cookie_Setting()
    username = user[0][0]
    pagenumber = int(pagenumber)
    offset_num = (pagenumber + 1) * 20
    statement = f"SELECT COUNT(*) from Thread WHERE Username = '{username}' LIMIT 20"
    cur.execute(statement)
    count = cur.fetchall()
    statement = f"SELECT Thread_ID, Title_Name, Username, Body_Text, Date_Made, Score from Thread WHERE Username = '{username}' LIMIT 20 OFFSET {offset_num};"
    cur.execute(statement)
    Saved_Threads = cur.fetchall()
    #DATABASE TO VARIABLES FOR THREADLIST -- done but not testing yet for displaying
    return template("saved.tpl", user=user, Saved_Threads=Saved_Threads, count=count, offset_num=offset_num)

@route('/newthread')
def newpost():
    user_session_id = request.get_cookie("user_session_id")
    user = sessions[user_session_id]
    username = user[0][0]
    statement = f"SELECT Username, Password, First_Name, Last_Name, Email_Address from Users WHERE Username='{username}';"
    cur.execute(statement)
    stored_info = cur.fetchall()
    return template('newthread.tpl', user=user, stored_info=stored_info, Email_Taken=False, Username_Taken=False, Not_Same_Password=False)

@route('/newpost/<threadnumber>')
def newpost(threadnumber):
    user_session_id = request.get_cookie("user_session_id")
    user = sessions[user_session_id]
    username = user[0][0]
    statement = f"SELECT Username, Password, First_Name, Last_Name, Email_Address from Users WHERE Username='{username}';"
    cur.execute(statement)
    stored_info = cur.fetchall()
    return template('newpost.tpl', threadnumber=threadnumber, user=user, stored_info=stored_info, Email_Taken=False, Username_Taken=False, Not_Same_Password=False)
        
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

run(host='localhost', port=8080, debug=True, reloader=True)
