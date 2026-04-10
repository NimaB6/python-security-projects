import hashlib
import getpass
import json
salt = "my_secret_salt"
def register():

    username=input("Input your User name : ")
    print("Type your password and press Enter. Nothing will appear on screen.")
    password=getpass.getpass("Input your Password : ")
    exists=False
    hashed_password = hashlib.sha256((password+salt).encode()).hexdigest()
    with open ("login_system/users.json","r") as file :
        users=json.load(file)
        if username in users :
            print("Username already exists")
            return
    users[username]=hashed_password
    
    with open("login_system/users.json", "w") as file:
        json.dump(users,file,indent=4)
        print("User registered successfully")
