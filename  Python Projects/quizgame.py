# Welcome message to the computer quiz
print("Welcome to my computer quiz!")

# Ask the user if they want to play
playing = input("Do you want to play? ")

# Check if the user does not want to play and quit if so
if playing.lower() != "yes":
    quit()

# Start the game
print("Okay! Let's play :)")
score = 0

# Ask the user the first question and check their answer
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Ask the user the second question and check their answer
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Ask the user the third question and check their answer
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Ask the user the fourth question and check their answer
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Display the final score
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
