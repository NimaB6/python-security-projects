import hashlib
import getpass
import json

salt = "my_secret_salt"

def login():
    attempts = 3

    while attempts > 0:
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()

        with open("login_system/users.json", "r") as file:
            users = json.load(file)

            if username in users and users[username] == hashed_password:
                print("Login successful ✅")
                return

            else:
                attempts -= 1

                if attempts > 0:
                    print(f"Wrong username or password ❌ ({attempts} attempts left)")
                else:
                    print("Too many attempts 🚫 Access denied")