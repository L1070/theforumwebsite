from bottle import route, run, template, request, SimpleTemplate
from bottle import response, post, get, delete, put, view, redirect, response, static_file
import uuid
import os, json, re
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
@route('/threadlist/page/0')
@route('/page/0')
@view('/')
def index():
    user = Cookie_Setting()
    statement = f"SELECT COUNT(*) from Thread WHERE isPinned = 0;"
    cur.execute(statement)
    count = cur.fetchall()
    count = count[0][0]
    statement = "SELECT Thread_ID, Title_Name, Username, Date_Made, Score, User_ID from Thread WHERE isPinned = 1;"
    cur.execute(statement)
    PinnedThreads = cur.fetchall()
    statement = "SELECT Thread_ID, Title_Name, Username, Date_Made, Score, User_ID from Thread WHERE isPinned = 0 LIMIT 20;"
    cur.execute(statement)
    UnPinnedThreads = cur.fetchall()
    #DATABASE TO VARIABLES FOR THREADLIST ----- Not displaying anything...
    user = Cookie_Setting()
    return template("index.tpl", user=user, PinnedThreads=PinnedThreads, UnPinnedThreads=UnPinnedThreads, count=count, offset_num=0, pagenumber=0)

@route('/threadlist/page/<pagenumber>')
@route('/page/<pagenumber>')
@view('/page/<pagenumber>')
def index(pagenumber):
    user = Cookie_Setting()
    statement = f"SELECT COUNT(*) from Thread WHERE isPinned = 0;"
    cur.execute(statement)
    count = cur.fetchall()
    count = count[0][0]
    pagenumber=int(pagenumber)
    offset_num = pagenumber * 20
    statement = f"SELECT Thread_ID, Title_Name, Username, Date_Made, Score, User_ID from Thread WHERE isPinned = 0 LIMIT 20 OFFSET {offset_num};"
    cur.execute(statement)
    UnPinnedThreads = cur.fetchall()
    #DATABASE TO VARIABLES FOR THREADLIST ------ Done, but not testing for displaying yet
    user = Cookie_Setting()
    return template("index.tpl", user=user, PinnedThreads="", UnPinnedThreads=UnPinnedThreads, count=count, offset_num=offset_num, pagenumber=pagenumber)

@route('/login')
def login():
    user = Cookie_Setting()
    return template('Login.tpl', LogInFailed=False, Registration_Success=False, user=user)

@route('/login', method='POST') 
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    statement = f"SELECT User_ID from users WHERE username='{username}' AND Password = '{password}';"
    cur.execute(statement)
    if not cur.fetchone():
        user = Cookie_Setting()
        return template("Login.tpl", LogInFailed=True, Registration_Success=False, user=user)
    user_session_id = str(uuid.uuid4())
    statement = f"SELECT Username, First_Name, Last_Name, Email_Address, Registered_Date, isAdmin, User_ID FROM Users Where Username = '{username}'"
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
    user = Cookie_Setting()
    statement = f"SELECT COUNT(*) from Comment WHERE Thread_ID = {threadnumber} AND isPinned = 0;"
    cur.execute(statement)
    count = cur.fetchall()
    count = count[0][0]
    statement = f"SELECT Title_Name from Thread WHERE Thread_ID = {threadnumber};"
    cur.execute(statement)
    threadtitle = cur.fetchall()
    threadtitle = threadtitle[0][0]
    statement = f"SELECT Comment_ID, Body_Text, Username, Date_Created, Score from Comment WHERE isPinned = 1 AND Thread_ID = {threadnumber};"
    cur.execute(statement)
    PinnedComments = cur.fetchall()
    statement = f"SELECT Comment_ID, Body_Text, Username, Date_Created, Score from Comment WHERE isPinned = 0 AND Thread_ID = {threadnumber} LIMIT 20;"
    cur.execute(statement)
    UnPinnedComments = cur.fetchall()
    user = Cookie_Setting()
    return template("threadpage.tpl", user=user, PinnedComments=PinnedComments, UnPinnedComments=UnPinnedComments, threadnumber=threadnumber, threadtitle=threadtitle, count=count, offset_num=0, pagenumber=0)
    
@route('/threadpage/<threadnumber>/<pagenumber>')
def threadpage(threadnumber, pagenumber):
    user = Cookie_Setting()
    statement = f"SELECT COUNT(*) from Comment WHERE Thread_ID = {threadnumber} AND isPinned = 0;"
    cur.execute(statement)
    count = cur.fetchall()
    count = count[0][0]
    pagenumber = int(pagenumber)
    offset_num = pagenumber * 20
    statement = f"SELECT Title_Name from Thread WHERE Thread_ID = {threadnumber};"
    cur.execute(statement)
    threadtitle = cur.fetchall()
    threadtitle = threadtitle[0][0]
    statement = f"SELECT Comment_ID, Body_Text, Username, Date_Created, Score from Comment WHERE isPinned = 0 AND Thread_ID = {threadnumber} LIMIT 20 OFFSET {offset_num};"
    cur.execute(statement)
    UnPinnedComments = cur.fetchall()
    user = Cookie_Setting()
    return template("threadpage.tpl", user=user, PinnedComments="", UnPinnedComments=UnPinnedComments, threadnumber=threadnumber, threadtitle=threadtitle, count=count, offset_num=offset_num, pagenumber=pagenumber)
    
@route('/useraccount')
def useraccount():
    user_session_id = request.get_cookie("user_session_id")
    user = sessions[user_session_id]
    user_ID = user[0][6]
    statement = f"SELECT Password from Users WHERE User_ID='{user_ID}';"
    cur.execute(statement)
    stored_info = cur.fetchone()
    #DATABASE TO VARIABLES FOR PREFILL USER ACCOUNT DETAILS -- done but not testing yet for displaying
    return template("useraccount.tpl", user=user, stored_info=stored_info, Email_Taken=False, Username_Taken=False, Not_Same_Password=False, Changes_Success=False)

@route('/useraccount', method='POST')
def do_changeaccount():
    user = Cookie_Setting()
    user_id = user[0][6]
    statement = f"SELECT Password from Users WHERE User_ID='{user_id}';"
    cur.execute(statement)
    stored_info = cur.fetchone()
    username = request.forms.get('username')
    password = request.forms.get('password')
    confirm_password = request.forms.get('confirm-password')
    first_name = request.forms.get('first-name')
    last_name = request.forms.get('last-name')
    email = request.forms.get('email-address')
    if password != confirm_password and stored_info[0] == password:
        return template('useraccount.tpl', Username_Taken=False, Email_Taken=False, Not_Same_Password=True, user=user, Changes_Success=False, stored_info=stored_info)
    elif password == confirm_password and stored_info[0] != password:
        statement = f"UPDATE USERS SET Password = '{password}' WHERE User_ID = {user_id}"
        cur.execute(statement)
        db.commit()
    statement = f"SELECT Username FROM Users WHERE Username = '{username}'"
    cur.execute(statement)
    if cur.fetchone() is not None and user[0][0] != username:
        return template('useraccount.tpl', Username_Taken=True, Email_Taken=False, Not_Same_Password=False, user=user, Changes_Success=False, stored_info=stored_info)
    else:
        statement = f"UPDATE USERS SET Username = '{username}' WHERE User_ID = {user_id}"
        cur.execute(statement)
        db.commit()
    statement = f"SELECT Email_Address FROM Users WHERE Email_Address = '{email}'"
    cur.execute(statement)
    if cur.fetchone() is not None and user[0][3] != email:
        return template('useraccount.tpl', Email_Taken=True, Username_Taken=False, Not_Same_Password=False, Changes_Success=False, user=user, stored_info=stored_info)
    else:
        statement = f"UPDATE USERS SET Email_Address = '{email}' WHERE User_ID = {user_id}"
        cur.execute(statement)
        db.commit()
    if user[0][1] != first_name:
        statement = f"UPDATE USERS SET First_Name = '{first_name}' WHERE User_ID = {user_id}"
        cur.execute(statement)
        db.commit()
    if user[0][2] != last_name:
        statement = f"UPDATE USERS SET Last_Name = '{last_name}' WHERE User_ID = {user_id}"
        cur.execute(statement)
        db.commit()
    user_session_id = str(uuid.uuid4())
    statement = f"SELECT Username, First_Name, Last_Name, Email_Address, Registered_Date, isAdmin, User_ID FROM Users Where Username = '{username}'"
    cur.execute(statement)
    sessions[user_session_id] = cur.fetchall()
    response.set_cookie("user_session_id", user_session_id)
    return template('useraccount.tpl', Email_Taken=False, Username_Taken=False, Not_Same_Password=False, Changes_Success=True, user=user, stored_info=stored_info)

@route('/saved')
@route('/saved/0')
def saved():
    user = Cookie_Setting()
    if user == "":
        return redirect("/");
    userid = user[0][6]
    statement = f"SELECT COUNT(*) from Saved WHERE User_ID = '{userid}';"
    cur.execute(statement)
    count = cur.fetchall()
    count = count[0][0]
    statement = f"SELECT Saved.Thread_ID, Title_Name, Username, Date_Made, Score, Thread.User_ID from Saved JOIN Thread ON Saved.Thread_ID=Thread.Thread_ID WHERE Saved.User_ID = '{userid}' LIMIT 20;"
    cur.execute(statement)
    Saved_Threads = cur.fetchall()
    #DATABASE TO VARIABLES FOR THREADLIST -- done but not testing yet for displaying
    return template("saved.tpl", user=user, Saved_Threads=Saved_Threads, count=count, offset_num=0, pagenumber=0)
        
@route('/saved/<pagenumber>')
def savedpage(pagenumber):
    user = Cookie_Setting()
    if user == "": 
        return redirect("/");
    userid = user[0][6]
    statement = f"SELECT COUNT(*) from Saved WHERE User_ID = '{userid}';"
    cur.execute(statement)
    count = cur.fetchall()
    count = count[0][0]
    pagenumber = int(pagenumber)
    offset_num = pagenumber * 20
    statement = f"SELECT Saved.Thread_ID, Title_Name, Username, Date_Made, Score, Thread.User_ID from Saved JOIN Thread ON Saved.Thread_ID=Thread.Thread_ID WHERE Saved.User_ID = '{userid}' LIMIT 20 OFFSET {offset_num};"
    cur.execute(statement)
    Saved_Threads = cur.fetchall()
    return template("saved.tpl", user=user, Saved_Threads=Saved_Threads, count=count, offset_num=offset_num, pagenumber=pagenumber)

@route('/newthread/<pagenumber>')
def newthread(pagenumber):
    user = Cookie_Setting()
    return template('newthread.tpl', user=user, pagenumber=pagenumber)

@route('/newthread/page/<pagenumber>', method='POST')
def do_newthread(pagenumber):
    user=Cookie_Setting()
    title=request.forms.get('title')
    content=request.forms.get('content')
    userid = user[0][6]
    username = user[0][0]
    content = re.sub(r'([0-9]{5})', r'</p><a href="/threadpage/\1" style="display:inline; color:var(--highlight);">\1</a><p style="display:inline;">', content)
    statement = f"INSERT INTO Thread (Title_Name, User_ID, Username, Date_Made) VALUES(?, ?, ?, datetime('now')) RETURNING Thread_ID;"
    data_tuple = (title, userid, username)
    cur.execute(statement, data_tuple)
    threadid = cur.fetchall()
    threadid = threadid[0][0]
    statement = f"INSERT INTO Comment (Thread_ID, User_ID, Username, Date_Created, Body_Text) VALUES (?, ?, ?, datetime('now'), ?);"
    data_tuple = (threadid, userid, username, content)
    cur.execute(statement, data_tuple)
    db.commit()
    pagenumber = str(pagenumber)
    wheretogo = '/page/' + pagenumber
    return redirect(wheretogo)

@route('/newpost/<threadnumber>/<pagenumber>')
def newpost(threadnumber, pagenumber):
    user = Cookie_Setting()
    return template('newpost.tpl', user=user, threadnumber=threadnumber, pagenumber=pagenumber)

@route('/newpost/<threadnumber>/<pagenumber>', method='POST')
def do_newpost(threadnumber, pagenumber):
    user=Cookie_Setting()
    content=request.forms.get('content')
    userid = user[0][6]
    username = user[0][0]
    content = re.sub(r'([0-9]{5})', r'</p><a href="/threadpage/\1" style="display:inline; color:var(--highlight);">\1</a><p style="display:inline;">', content)
    threadid = threadnumber
    statement = f"INSERT INTO Comment (Thread_ID, User_ID, Username, Date_Created, Body_Text) VALUES (?, ?, ?, datetime('now'), ?);"
    data_tuple = (threadid, userid, username, content)
    cur.execute(statement, data_tuple)
    db.commit()
    threadid = str(threadid)
    pagenumber = str(pagenumber)
    wheretogo = '/threadpage/' + threadid + '/' + pagenumber
    return redirect(wheretogo)
    
@route('/savethread/<threadtype>/page/<pagenumber>', method='POST')
def button_savethread(threadtype, pagenumber):
    userid=Cookie_Setting()
    userid=userid[0][6]
    threadid=request.forms.get('threadid')
    statement = f"SELECT * FROM Saved WHERE Thread_ID = {threadid} AND User_ID = {userid};"
    cur.execute(statement)
    if cur.fetchone() is not None:
        statement = f"DELETE FROM Saved WHERE Thread_ID = {threadid} AND User_ID = {userid};"
        cur.execute(statement)
    else:
        statement = f"INSERT INTO Saved (Thread_ID, User_ID) VALUES (?, ?);"
        data_tuple = (threadid, userid)
        cur.execute(statement, data_tuple)
    db.commit()
    pagenumber = str(pagenumber)
    if threadtype == 'home':
        wheretogo = '/page/' + pagenumber
    elif threadtype == 'saved':
        wheretogo = '/saved/' + pagenumber
    return redirect(wheretogo)
    
@route('/deletethread/<threadtype>/page/<pagenumber>', method='POST')
def button_deletethread(threadtype, pagenumber):
    userid=Cookie_Setting()
    userid=userid[0][6]
    threadid=request.forms.get('threadid')
    statement = f"DELETE FROM Thread WHERE Thread_ID = {threadid};"
    cur.execute(statement)
    statement = f"DELETE FROM Comment WHERE Thread_ID = {threadid};"
    cur.execute(statement)
    statement = f"DELETE FROM Saved WHERE Thread_ID = {threadid};"
    cur.execute(statement)
    db.commit()
    pagenumber = str(pagenumber)
    if threadtype == 'home':
        wheretogo = '/page/' + pagenumber
    elif threadtype == 'saved':
        wheretogo = '/saved/' + pagenumber
    return redirect(wheretogo)
    
@route('/deletecomment/<threadid>/page/<pagenumber>', method='POST')
def button_deletecomment(threadid, pagenumber):
    userid=Cookie_Setting()
    userid=userid[0][6]
    commentid=request.forms.get('commentid')
    statement = f"DELETE FROM Comment WHERE Comment_ID = {commentid};"
    cur.execute(statement)
    db.commit()
    pagenumber = str(pagenumber)
    threadid = str(threadid)
    wheretogo = '/threadpage/' + threadid + '/' + pagenumber
    return redirect(wheretogo)
    
@route('/pinthread/<threadtype>/page/<pagenumber>', method='POST')
def button_pinthread(threadtype, pagenumber):
    userid=Cookie_Setting()
    userid=userid[0][6]
    threadid=request.forms.get('threadid')
    statement = f"SELECT isPinned FROM Thread WHERE Thread_ID = {threadid};"
    cur.execute(statement)
    ispinned = cur.fetchall()
    ispinned = ispinned[0][0]
    if ispinned == 0:
        statement = f"UPDATE Thread SET isPinned = 1 WHERE Thread_ID = {threadid};"
    else:
        statement = f"UPDATE Thread SET isPinned = 0 WHERE Thread_ID = {threadid};"
    cur.execute(statement)
    db.commit()
    pagenumber = str(pagenumber)
    if threadtype == 'home':
        wheretogo = '/page/' + pagenumber
    elif threadtype == 'saved':
        wheretogo = '/saved/' + pagenumber
    return redirect(wheretogo)
    
@route('/pincomment/<threadid>/page/<pagenumber>', method='POST')
def button_pincomment(threadid, pagenumber):
    userid=Cookie_Setting()
    userid=userid[0][6]
    commentid=request.forms.get('commentid')
    statement = f"SELECT isPinned FROM Comment WHERE Comment_ID = {commentid};"
    cur.execute(statement)
    ispinned = cur.fetchall()
    ispinned = ispinned[0][0]
    if ispinned == 0:
        statement = f"UPDATE Comment SET isPinned = 1 WHERE Comment_ID = {commentid};"
    else:
        statement = f"UPDATE Comment SET isPinned = 0 WHERE Comment_ID = {commentid};"
    cur.execute(statement)
    db.commit()
    pagenumber = str(pagenumber)
    threadid = str(threadid)
    wheretogo = '/threadpage/' + threadid + '/' + pagenumber
    return redirect(wheretogo)

@route('/<threadnumber>/up/<threadtype>/page/<pagenumber>', method='POST')
@route('/<threadnumber>/up/<threadtype>/page/<pagenumber>', method='GET')
def up_button(threadnumber, threadtype, pagenumber):
    user = Cookie_Setting()
    user_id = user[0][6]
    statement = f"SELECT Score FROM Thread WHERE Thread_ID = {threadnumber};"
    cur.execute(statement)
    score = cur.fetchone()
    score = score[0]
    statement = f"SELECT Status FROM Thread_Likes WHERE Thread_ID = {threadnumber} AND User_ID = {user_id};"
    cur.execute(statement)
    status = cur.fetchone()
    if status is not None and status[0] != 0:
        if status[0] == 1:
            score = score - 1
            statement = f"UPDATE Thread SET Score = {score} WHERE Thread_ID = {threadnumber};"
            cur.execute(statement)
            db.commit()
            status = status[0]
            status = 0
            statement = f"UPDATE Thread_Likes SET Status = {status} WHERE Thread_ID = {threadnumber} AND User_ID = {user_id};"
            cur.execute(statement)
            db.commit()
            pagenumber = str(pagenumber)
            if threadtype == 'home':
                wheretogo = '/page/' + pagenumber
            elif threadtype == 'saved':
                wheretogo = '/saved/' + pagenumber
            return redirect(wheretogo)
        elif status[0] == -1:
            score = score + 2
            statement = f"UPDATE Thread SET Score = {score} WHERE Thread_ID = {threadnumber};"
            cur.execute(statement)
            db.commit()
            status = status[0]
            status = 1
            statement = f"UPDATE Thread_Likes SET Status = {status} WHERE Thread_ID = {threadnumber} AND User_ID = {user_id};"
            cur.execute(statement)
            db.commit()
            pagenumber = str(pagenumber)
            if threadtype == 'home':
                wheretogo = '/page/' + pagenumber
            elif threadtype == 'saved':
                wheretogo = '/saved/' + pagenumber
            return redirect(wheretogo)
    score = score + 1
    statement = f"UPDATE Thread SET Score = {score} WHERE Thread_ID = {threadnumber};"
    cur.execute(statement)
    db.commit()
    if status is not None and status[0] == 0:
        statement = f"UPDATE Thread_Likes SET Status = 1 WHERE Thread_ID = {threadnumber} AND User_ID = {user_id};"
        cur.execute(statement)
        db.commit()
    else:
        statement = f"INSERT INTO Thread_Likes (Status, Thread_ID, User_ID) VALUES (?,?,?);"
        data_tuple = (1, threadnumber, user_id)
        cur.execute(statement, data_tuple)
        db.commit()
    pagenumber = str(pagenumber)
    if threadtype == 'home':
        wheretogo = '/page/' + pagenumber
    elif threadtype == 'saved':
        wheretogo = '/saved/' + pagenumber
    return redirect(wheretogo)

@route('/<threadnumber>/down/<threadtype>/page/<pagenumber>', method='POST')
@route('/<threadnumber>/down/<threadtype>/page/<pagenumber>', method='GET')
def down_button(threadnumber, threadtype, pagenumber):
    user = Cookie_Setting()
    user_id = user[0][6]
    statement = f"SELECT Score FROM Thread WHERE Thread_ID = {threadnumber};"
    cur.execute(statement)
    score = cur.fetchone()
    score = score[0]
    statement = f"SELECT Status FROM Thread_Likes WHERE Thread_ID = {threadnumber} AND User_ID = {user_id};"
    cur.execute(statement)
    status = cur.fetchone()
    if status is not None and status[0] != 0:
        if status[0] == -1:
            score = score + 1
            statement = f"UPDATE Thread SET Score = {score} WHERE Thread_ID = {threadnumber};"
            cur.execute(statement)
            db.commit()
            status = status[0]
            status = 0
            statement = f"UPDATE Thread_Likes SET Status = {status} WHERE Thread_ID = {threadnumber} AND User_ID = {user_id};"
            cur.execute(statement)
            db.commit()
            pagenumber = str(pagenumber)
            if threadtype == 'home':
                wheretogo = '/page/' + pagenumber
            elif threadtype == 'saved':
                wheretogo = '/saved/' + pagenumber
            return redirect(wheretogo)
        elif status[0] == 1:
            score = score - 2
            statement = f"UPDATE Thread SET Score = {score} WHERE Thread_ID = {threadnumber};"
            cur.execute(statement)
            db.commit()
            status = status[0]
            status = -1
            statement = f"UPDATE Thread_Likes SET Status = {status} WHERE Thread_ID = {threadnumber} AND User_ID = {user_id};"
            cur.execute(statement)
            db.commit()
            pagenumber = str(pagenumber)
            if threadtype == 'home':
                wheretogo = '/page/' + pagenumber
            elif threadtype == 'saved':
                wheretogo = '/saved/' + pagenumber
            return redirect(wheretogo)
    score = score - 1
    statement = f"UPDATE Thread SET Score = {score} WHERE Thread_ID = {threadnumber};"
    cur.execute(statement)
    db.commit()
    if status is not None and status[0] == 0:
        statement = f"UPDATE Thread_Likes SET Status = -1 WHERE Thread_ID = {threadnumber} AND User_ID = {user_id};"
        cur.execute(statement)
        db.commit()
    else:
        statement = f"INSERT INTO Thread_Likes (Status, Thread_ID, User_ID) VALUES (?,?,?);"
        data_tuple = (-1, threadnumber, user_id)
        cur.execute(statement, data_tuple)
        db.commit() 
    pagenumber = str(pagenumber)
    if threadtype == 'home':
        wheretogo = '/page/' + pagenumber
    elif threadtype == 'saved':
        wheretogo = '/saved/' + pagenumber
    return redirect(wheretogo)

@route('/<commentnumber>/commentup/<threadid>/page/<pagenumber>', method='POST')
@route('/<commentnumber>/commentup/<threadid>/page/<pagenumber>', method='GET')
def up_button(commentnumber, threadid, pagenumber):
    user = Cookie_Setting()
    user_id = user[0][6]
    statement = f"SELECT Score FROM Comment WHERE Comment_ID = {commentnumber};"
    cur.execute(statement)
    score = cur.fetchone()
    score = score[0]
    statement = f"SELECT Status FROM Comment_Likes WHERE Comment_ID = {commentnumber} AND User_ID = {user_id};"
    cur.execute(statement)
    status = cur.fetchone()
    if status is not None and status[0] != 0:
        if status[0] == 1:
            score = score - 1
            statement = f"UPDATE Comment SET Score = {score} WHERE Comment_ID = {commentnumber};"
            cur.execute(statement)
            db.commit()
            status = status[0]
            status = 0
            statement = f"UPDATE Comment_Likes SET Status = {status} WHERE Comment_ID = {commentnumber} AND User_ID = {user_id};"
            cur.execute(statement)
            db.commit()
            pagenumber = str(pagenumber)
            threadid = str(threadid)
            wheretogo = '/threadpage/' + threadid + '/' + pagenumber
            return redirect(wheretogo)
        elif status[0] == -1:
            score = score + 2
            statement = f"UPDATE Comment SET Score = {score} WHERE Comment_ID = {commentnumber};"
            cur.execute(statement)
            db.commit()
            status = status[0]
            status = 1
            statement = f"UPDATE Comment_Likes SET Status = {status} WHERE Comment_ID = {commentnumber} AND User_ID = {user_id};"
            cur.execute(statement)
            db.commit()
            pagenumber = str(pagenumber)
            threadid = str(threadid)
            wheretogo = '/threadpage/' + threadid + '/' + pagenumber
            return redirect(wheretogo)
    score = score + 1
    statement = f"UPDATE Comment SET Score = {score} WHERE Comment_ID = {commentnumber};"
    cur.execute(statement)
    db.commit()
    if status is not None and status[0] == 0:
        statement = f"UPDATE Comment_Likes SET Status = 1 WHERE Comment_ID = {commentnumber} AND User_ID = {user_id};"
        cur.execute(statement)
        db.commit()
    else:
        statement = f"INSERT INTO Comment_Likes (Status, Comment_ID, User_ID) VALUES (?,?,?);"
        data_tuple = (1, commentnumber, user_id)
        cur.execute(statement, data_tuple)
        db.commit()
    pagenumber = str(pagenumber)
    threadid = str(threadid)
    wheretogo = '/threadpage/' + threadid + '/' + pagenumber
    return redirect(wheretogo)

@route('/<commentnumber>/commentdown/<threadid>/page/<pagenumber>', method='POST')
@route('/<commentnumber>/commentdown/<threadid>/page/<pagenumber>', method='GET')
def down_button(commentnumber, threadid, pagenumber):
    user = Cookie_Setting()
    user_id = user[0][6]
    statement = f"SELECT Score FROM Comment WHERE Comment_ID = {commentnumber};"
    cur.execute(statement)
    score = cur.fetchone()
    score = score[0]
    statement = f"SELECT Status FROM Comment_Likes WHERE Comment_ID = {commentnumber} AND User_ID = {user_id};"
    cur.execute(statement)
    status = cur.fetchone()
    if status is not None and status[0] != 0:
        if status[0] == -1:
            score = score + 1
            statement = f"UPDATE Comment SET Score = {score} WHERE Comment_ID = {commentnumber};"
            cur.execute(statement)
            db.commit()
            status = status[0]
            status = 0
            statement = f"UPDATE Comment_Likes SET Status = {status} WHERE Comment_ID = {commentnumber} AND User_ID = {user_id};"
            cur.execute(statement)
            db.commit()
            pagenumber = str(pagenumber)
            threadid = str(threadid)
            wheretogo = '/threadpage/' + threadid + '/' + pagenumber
            return redirect(wheretogo)
        elif status[0] == 1:
            score = score - 2
            statement = f"UPDATE Comment SET Score = {score} WHERE Comment_ID = {commentnumber};"
            cur.execute(statement)
            db.commit()
            status = status[0]
            status = -1
            statement = f"UPDATE Comment_Likes SET Status = {status} WHERE Comment_ID = {commentnumber} AND User_ID = {user_id};"
            cur.execute(statement)
            db.commit()
            pagenumber = str(pagenumber)
            threadid = str(threadid)
            wheretogo = '/threadpage/' + threadid + '/' + pagenumber
            return redirect(wheretogo)
    score = score - 1
    statement = f"UPDATE Comment SET Score = {score} WHERE Comment_ID = {commentnumber};"
    cur.execute(statement)
    db.commit()
    if status is not None and status[0] == 0:
        statement = f"UPDATE Comment_Likes SET Status = -1 WHERE Comment_ID = {commentnumber} AND User_ID = {user_id};"
        cur.execute(statement)
        db.commit()
    else:
        statement = f"INSERT INTO Comment_Likes (Status, Comment_ID, User_ID) VALUES (?,?,?);"
        data_tuple = (-1, commentnumber, user_id)
        cur.execute(statement, data_tuple)
        db.commit() 
    pagenumber = str(pagenumber)
    threadid = str(threadid)
    wheretogo = '/threadpage/' + threadid + '/' + pagenumber
    return redirect(wheretogo)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

run(host='localhost', port=8080, debug=True, reloader=True)
