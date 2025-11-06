correct_password = "12345"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    entry = input("Enter the password: ")
    if entry == correct_password:
        print("Access granted. Correct password entered.")
        break
    else:zdfdsf
        attempts = attempts + 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print("Wrong password. " + str(remaining) + " attempts remaining.")
        else:
            print("Maximum attempts reached. Authorities have been alerted.")
