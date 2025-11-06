name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")
age = input("Enter your age: ")

biography = {
    "Name": name,
    "Hometown": hometown,
    "Age": age
}

print("Name: " + biography["Name"] + "\nHometown: " + biography["Hometown"] + "\nAge: " + biography["Age"])
