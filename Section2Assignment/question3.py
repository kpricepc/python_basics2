import random

def HeartsSpades():
    # Print rules
    print("Hearts and Spades Game!")
    print("For every digit you guess correctly in the correct place, you get a heart.")
    print("For every digit you guess correctly in the wrong place is a spade.")

    # Create counter and lists to use
    guessCount = 0
    guesses = list()
    NUMBER = list()

    # Create 4 random numbers in a list that are unique
    x = False
    while x == False:
        # Generate 4 numbers in a list
        for i in range(4):
            NUMBER.append(str(random.randint(0, 9)))
        # Check that numbers are unique    
        if(len(set(NUMBER))) == len(NUMBER):
            x = True
        else:
            # Empty the list if not unique and loop through trying again
            NUMBER = []
            x = False
    
    # Print the randomly generated list
    print("For Testing Purposes, the answer is " + str(NUMBER))
    while True:
        try:
            # User enters a number
            guess = input("Enter a number: ")

            # Verify user enters a 4 digit number
            if isinstance(int(guess), int) is not True or int(guess) < 0 or len(guess) != 4 or guess in guesses:
                raise Exception
        except Exception:
            print("Please be sure to make your guess a 4-digit integer number (0000 - 9999) and numbers are unique.")
        else:
            guesses.append(guess)
            hearts = 0
            spades = 0
            guessCount += 1
            
            # Check Hearts
            heartList = [0,0,0,0]
            for i in range(4):
                if NUMBER[i] == guess[i]:
                    hearts += 1
                    heartList[i] = 1 

            # Check Spades
            spadeList = [0,0,0,0]

            # Loop over NUMBER to see if guess digits exist
            for i in range(4):

                # Continue if NUMBER digit (variable i) is a Heart
                if heartList[i] == 1:
                    continue

                # Loop over guess digits to see if they match NUMBER[i]
                for j in range(4):

                    # Continue if NUMBER digit (variable i) is a spade
                    if spadeList[i] == 1:
                        continue
                    
                    # If guess digit is in the NUMBER, store the postion of the number list spade so it isn't double counted next time
                    if guess[j] == NUMBER[i]:
                        spades += 1
                        heartList[i] = 1

            # Print Output of Hearts + Spades           
            print(str(hearts) + ' hearts, ' + str(spades) + ' spades')
      
            # User got all Correct
            if hearts == 4:
                return print('You won in ' + str(guessCount) + ' guesses!')

# Start Program
HeartsSpades()