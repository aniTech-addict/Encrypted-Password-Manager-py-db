import sqlite3
from encryption_handler  import xor_encrypt_decrypt

class PasswordManager :
    def __init__(self, db_name , master_key):
        self.db_name = db_name
        self.master_key = master_key
        self.init_db()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def init_db(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(
            '''
                CREATE TABLE IF NOT EXISTS passwords(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
                )
            '''
        )


        conn.commit()
        conn.close
    def add_password(self,acc_name, password):
        encrypted_password = xor_encrypt_decrypt(password,self.master_key)

        conn= self.connect()
        cursor = conn.cursor()

        cursor.execute('INSERT INTO passwords (username,password) VALUES(?,?)',(acc_name,encrypted_password))

        conn.commit()
        conn.close()
        print("Password Saved")





