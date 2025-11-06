names = ["Jake","jake", "Zac","zac", "Ian","ian", "Ron","ron", "Sam","sam", "Dave","dave"]

search_name = input("Enter the name you want to search for: ")

if search_name in names:
    print(search_name + " is in the list!")
else:
    print(search_name + " is not in the list.")