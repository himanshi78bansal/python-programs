import sqlite3

db = sqlite3.connect("student.db")
cursor = db.cursor()
cursor.execute("create table st(id integer primary key, name, text, age integer)")
db.commit()
db.close()
