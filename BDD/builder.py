import sqlite3

con = sqlite3.connect('bot_base.db')
cur = con.cursor()

cur.execute('''CREATE TABLE user (name_user text, id_user real)''')

con.commit()
con.close()