ask = input("Would you like to play a game? ")
if ask.lower() == "yes":
    print("Great!")
else:
    print("You must be scared")
    quit()
score = 0
ask1 = input("How many States in America? ")
if ask1.lower() == "50":
    print("Corrrect :)")
    score += 1
else:
    print("Incorrect :(")

ask2 = input("Who is the best NFL team? ")
if ask2.lower() == "steelers":
    print("My man!")
    score += 1
else:
    print("Incorrect!")

ask3 = input("Where is the White House located? ")
if ask3.lower() == "dc":
    print("Correct!")
    score += 1
else:
    print("Sorry wrong answer")

ask4 = input("What color is the sky? ")
if ask4.lower() == "blue":
    print("Correct :)")
    score += 1
else:
    print("Really? :(")
print()
print("You got " + str(score) + " Right" )
print(str(score/4 * 100) + "%")
