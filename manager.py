import random
import sqlite3
from encryption_handler  import xor_encrypt_decrypt
import string
import random

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
        conn.close()
        

# Operational Methods 
        
    def view_passwords(self):
        """
        Connects to the database, fetches all username and encrypted password pairs from the 'passwords' table,
        decrypts each password using the master key
        prints them to the console.
        
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute('SELECT username,password FROM passwords')
        rows = cursor.fetchall()
        
        for username,encrypted_password in rows:
            password = xor_encrypt_decrypt(encrypted_password.strip(),self.master_key)
            print(f"Username: {username}\n Password: {password}\n")
        
        toContinue = input()
        
        conn.close()
        
        
    def add_password(self,acc_name, password):
        encrypted_password = xor_encrypt_decrypt(password,self.master_key)

        conn= self.connect()
        cursor = conn.cursor()

        cursor.execute('INSERT INTO passwords (username,password) VALUES(?,?)',(acc_name,encrypted_password))

        conn.commit()
        conn.close()
        print("Password Saved")
        toContinue = input()
        
    def search_password(self,acc_name):
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute('SELECT username,password FROM passwords WHERE username LIKE ?',(f"%{acc_name}%",))
        
        rows = cursor.fetchall()
        if rows == []:
            print("No Such Username Found")
            
        
        for username,encrypted_password in rows:
            password = xor_encrypt_decrypt(encrypted_password.strip(),self.master_key)
            
            print(f"    Username: {username}\n  Password: {password}\n")
        
        to_continue = input()    
            
        conn.close()
    
    def generate_random_password(self):
        
        MAX_PASSOWRD_LEN = 22
        
        special_characters = ["@","#","&","!"]
        digits = string.digits
        upper_case = string.ascii_uppercase
        lower_case = string.ascii_lowercase
        
        password_map = [special_characters, digits, upper_case, lower_case]
        
        for_diversity = [random.choice(digits),
                         random.choice(upper_case),
                         random.choice(lower_case),
                         random.choice(special_characters)]

        huh = [random.choice(random.choice(password_map)) for _ in range(MAX_PASSOWRD_LEN-len(for_diversity))]
        for_diversity.extend(huh)
        random.shuffle(for_diversity)
        generated_password = "".join(for_diversity)
        print(generated_password)
        
        use_genrated_password = input("Use this genrated password ?? (y/n)")
        if use_genrated_password == "y":
            username = input("Enter your Username")
            self.add_password(username,generated_password)
        
        
        
        
        
                
            


# %%
