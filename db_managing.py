import sqlite3
import os
import datetime

connect = sqlite3.connect('results.db')
def create_cursor():
    global cursor
    if not os.path.exists('results.db'): 
        cursor = connect.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS results(score INT, name TEXT, date TEXT)')
    else:
        cursor = connect.cursor()
    return cursor

cursor = create_cursor()
username = os.environ.get("USERNAME")

def get_cursor():
    cursor = connect.cursor()
    return cursor

def commit_connect():
    connect.commit()

def insert_result_into_db(score):
    global username
    now = datetime.datetime.now()
    date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

    sqlite_insert_with_param = """INSERT INTO results
                          (score, name, date) 
                          VALUES (?, ?, ?);"""
    data_tuple = (score, username, date)
    curs = get_cursor()
    curs.execute(sqlite_insert_with_param, data_tuple)

def your_best_result():
    global cursor, username
    cursor.execute('''SELECT MAX(score) FROM results
    WHERE name=(?)''', (username,))
    best = cursor.fetchall()
    return best[0][0]

def best_result():
    global cursor, username
    cursor.execute('''SELECT MAX(score) FROM results''')
    best_ovr = cursor.fetchall()
    return best_ovr[0][0]

def your_average():
    global cursor, username
    cursor.execute('''SELECT AVG(score) FROM results
    WHERE name=(?)''', (username,))
    avg = cursor.fetchall()
    return avg[0][0]

def get_username():
    uname = os.environ.get("USERNAME")
    return uname

def db_reset():
    cursor = connect.cursor()
    cursor.execute("DELETE FROM results")