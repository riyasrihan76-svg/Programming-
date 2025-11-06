
score = 0

quiz = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Switzerland": "Bern"
}

for country in quiz:
    answer = input("What is the capital of " + country + "? ")

    if answer == quiz[country] or answer.lower() == quiz[country].lower():
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is " + quiz[country] + ".")

print("\nYou got " + str(score) + " out of " + str(len(quiz)) + " correct!")
