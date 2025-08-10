password_file = open("TextPassword.txt")
secret_password = password_file.read()
print("enter your password")
typed_password = input()
if typed_password == secret_password:
    print("Access granted")
    if typed_password == "1234":
        print("Stupid password")
    else:
        print("Access denied")
