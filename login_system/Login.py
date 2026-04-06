import hashlib
import getpass
def login():
    attempts=3
    while (attempts>0) :
        username=input("Input your User name : ")
        print("Type your password and press Enter. Nothing will appear on screen.")
        password=getpass.getpass("Input your Password : ")
        hashed_password=hashlib.md5(password.encode()).hexdigest()
        found=False
        with open ("login_system/users.txt","r") as file :
            for line in file:
                stored_username, stored_password=line.strip().split(",")
                if(stored_username==username and stored_password==hashed_password):
                    found=True
                    print("Login successful!!")
                    return

        attempts -= 1

        if attempts > 0:
            print(f"Wrong username or password ({attempts} attempts left)")
        else:
            print("Too many attempts. Access denied")
