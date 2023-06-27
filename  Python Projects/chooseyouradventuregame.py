# Prompt the user to input their name and greet them
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

# Ask the user to choose a direction (left or right)
answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

# Check if the user chose to go left
if answer == "left":
    # Ask the user how they want to cross the river
    answer = input(
        "You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")

    # Check if the user chose to swim
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    # Check if the user chose to walk
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

# Check if the user chose to go right
elif answer == "right":
    # Ask the user if they want to cross the bridge or go back
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    # Check if the user chose to go back
    if answer == "back":
        print("You go back and lose.")
    # Check if the user chose to cross the bridge
    elif answer == "cross":
        # Ask the user if they want to talk to a stranger
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        # Check if the user chose to talk to the stranger
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        # Check if the user chose not to talk to the stranger
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

# Thank the user for playing the game
print("Thank you for trying", name)
