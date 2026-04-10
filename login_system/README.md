# 🔐 Login System

A simple Python login system with registration, login, password hashing, salt, and JSON-based user storage.

---

## 🚀 Features

- User registration
- User login
- Password hashing
- Salt for stronger password protection
- User data stored in JSON
- Limited login attempts
- Simple main menu

---

## 📂 Project Structure

```text
login_system/
├── register.py
├── login.py
├── main.py
└── users.json
```

---

## ⚙️ How It Works

### Register
- The user enters a username and password
- The password is hashed with salt
- The username and hashed password are stored in `users.json`

### Login
- The user enters username and password
- The system hashes the entered password with the same salt
- If the stored data matches, login is successful

---

## 🔐 Security Notes

- Passwords are **not stored in plain text**
- Passwords are hashed before saving
- Salt is used to improve security
- Login attempts are limited

---

## ▶️ Usage

Run the main file:

```bash
python main.py
```

Then choose:

- Register
- Login
- Exit

---

## 🛠 Technologies Used

- Python
- hashlib
- json
- getpass

---

## 👨‍💻 Author

Mohammadhosein(Nima) Bahrami