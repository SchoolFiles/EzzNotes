import sqlite3
import os

root = os.path.dirname(os.path.relpath((__file__)))

def access_site(username, email, password):
    con = sqlite3.connect(os.path.join(root,"Archivio.db"))
    cur = con.cursor()

    result = cur.execute("SELECT password FROM user WHERE username = ?", username)

    if (result == password){
        # Loged in
        return True
    }


    pass

