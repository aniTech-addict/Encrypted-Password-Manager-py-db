# Python Password Manager 🔐

A simple, CLI-based password manager built in Python with SQLite integration.  
Store, view, and search your encrypted passwords—all in one place.

---

## 🚀 Why This Exists

Ever felt like juggling text files is a nightmare?  
This project moves you from `psw.txt` chaos to a clean SQLite database.  
You’ll learn how to:
- Set up a local SQLite DB in Python
- Encrypt/decrypt passwords with XOR
- Build a modular class-based design
- Interact via a straightforward CLI

---

## 🛠️ Features

- **Add New Password**  
  Encrypts your password with a master key, then saves it to `passwords.db`.

- **View All Passwords**  
  Decrypts and lists every stored account + its password.

- **Search by Username**  
  Quickly find a specific account using SQL’s `LIKE` query.

- **Master Key Protection**  
  You choose a 6–15 character master key on startup—no key, no access.

---

## 📦 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. (Optional) Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3. Install Requirements
There’s only one external library (if you extract XOR to its own file, otherwise it’s pure stdlib):

bash
Copy
Edit
pip install -r requirements.txt
Note: If you only use built-in sqlite3 and custom XOR, you might not need any dependencies.

⚙️ Usage
Run the app:

bash
Copy
Edit
python main.py
Enter Master Key:

Must be 6–15 characters.

This key encrypts/decrypts all your entries.

Choose an Option:

1: View Passwords

2: Add New Password

3: Search Password

4: Quit

Follow Prompts:

When adding, type the account name (e.g., gmail) and the actual password.

When searching, type part or all of the username to filter results.

Exit:

Option 4 closes the app.

📁 Project Structure
vbnet
Copy
Edit
.
├── main.py              # CLI interface + input validation
├── manager.py           # PasswordManager class (DB logic + XOR calls)
├── encryption_handler.py # XOR encrypt/decrypt function
├── passwords.db         # SQLite database (auto-generated)
├── requirements.txt     # (Empty or contains dependencies)
└── README.md
🔍 How It Works (Under the Hood)
Database Initialization

On startup, PasswordManager.init_db() creates passwords table if missing.

Adding a Password

PasswordManager.add_password(username, raw_password)

XOR-encrypts raw_password with your master key.

Inserts (username, encrypted_password) into SQLite.

Viewing Passwords

PasswordManager.view_passwords()

Runs SELECT username, password FROM passwords.

Decrypts each password before printing.

Searching

PasswordManager.search_password(term)

Runs SELECT username, password FROM passwords WHERE username LIKE '%term%'.

Decrypts and shows matching results.

🔧 Troubleshooting
“No data shows up”

Make sure you’re in the same directory where passwords.db lives.

Check that your master key matches what you used when adding entries.

“I see multiple DB files”

Use an absolute path in main.py to lock down where passwords.db is created:

python
Copy
Edit
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "passwords.db")
pm = PasswordManager(DB_PATH, master_key)
“I typed letters instead of numbers in the menu”

The CLI expects an integer. If you type non-numeric input, it’ll reprompt.

🏗️ Next Steps & Improvements
Stronger Encryption
Replace XOR with something like cryptography.Fernet for serious security.

Unique Constraints
Enforce unique usernames or allow multiple entries per account with tags.

GUI/Web Frontend
Build a Tkinter/Flask front end so you can click buttons instead of typing commands.

Master Key Hashing
Store a hash of the master key so you can verify it on startup (instead of trusting the user).
