import random

MINIMUM = 0
MAXIMUM = 100

# Generate Random Number
NUMBER = random.randint(MINIMUM, MAXIMUM)

ATTEMPTS = int(input("How many attempts would you like? "))

print("Starting Game with " + str(ATTEMPTS) + " attempts")
 
# Initializing the number of guesses.
GUESS_COUNT = 0
 
# for calculation of minimum number of
# guesses depends upon range
while ATTEMPTS > 0:
    ATTEMPTS -= 1
    GUESS_COUNT += 1
    # taking guessing number as input
    GUESS_USER = int(input("Guess a number: "))
 
    # Condition Testing
    if NUMBER == GUESS_USER:
        print("Congratulations!!")
        print("The number is " + str(NUMBER) + " and you did it in " + str(GUESS_COUNT) + " trys!")
        # Once number is guessed, break the loop
        break
    # Give user feedback if number is too small
    elif NUMBER > GUESS_USER:
        print("Your guess is too small!")
    # Give user feedback if number is too large
    elif NUMBER < GUESS_USER:
        print("Your guess is too high!")
 
# Once number of attempts equlas 0, show the number.
if ATTEMPTS == 0:
    print("The number is " + str(NUMBER))
    print("Good luck next time!")