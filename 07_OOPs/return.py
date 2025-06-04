def painter():
    return "I am a painter"
print(painter())

def validate():
    if username == "admin" and password == "1234":
        return True
    else:
        return False
    
username = input("Enter username: ")
password = input("Enter password: ")

if validate():
    print("Access granted")
else:
    print("Access denied")

