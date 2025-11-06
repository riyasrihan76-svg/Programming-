password = "12345"

while True:
    entry = input("Enter the password: ")
    if entry == password:
        print("Access granted. Correct password entered.")
        break
    else:
        print("Wrong password. Try again.")
