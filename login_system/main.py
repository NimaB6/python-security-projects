from register import register as re
from Login import login as le 


while True:
    print("\n" + "="*40)
    print("🔐 LOGIN SYSTEM")
    print("="*40)

    print("1️⃣  Register")
    print("2️⃣  Login")
    print("3️⃣  Exit")

    print("="*40)

    choice = input("👉 Enter your choice: ")

    if choice == "1":
        print("\n📝 Register selected\n")
        re()
    elif choice == "2":
        print("\n🔑 Login selected\n")
        le()
    elif choice == "3":
        print("\n👋 Goodbye!\n")
        break
    else:
        print("\n❌ Invalid choice, try again!\n")