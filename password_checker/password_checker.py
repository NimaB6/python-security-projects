password=input("Enter your password: ")
errors=[]
has_upper = False
has_lower = False
has_digit = False
has_symbol = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_symbol = True

if len(password) < 8:
    errors.append("Password must be at least 8 characters long")

if not has_upper:
    errors.append("Password must contain at least one uppercase letter")

if not has_lower:
    errors.append("Password must contain at least one lowercase letter")

if not has_digit:
    errors.append("Password must contain at least one number")

if not has_symbol:
    errors.append("Password must contain at least one symbol")

if len(errors) == 0:
    print("Strong password")
else:
    print("Weak password")
    print("Problems found:")
    for  error in errors:
        print("-",error)