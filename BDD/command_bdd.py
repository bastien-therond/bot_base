import sqlite3

class command_bdd(object):

    def __init__(self):
        self.con = sqlite3.connect("BDD/bot_base.db")

    @property
    def getAllUser(self):
        cur = self.con.cursor()
        rep = cur.execute("""select * from user""")
        self.con.commit()
        return rep

    def getOneUserById(self, attr):
        cur = self.con.cursor()
        cur.execute()
        return self.con.execute("""select * from user where """)