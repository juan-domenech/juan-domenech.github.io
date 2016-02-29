import random
NUMBER_OF_GUESSES = 10
RANGE_START = 1
RANGE_END = 20
while True:

    print "\nLet's play!"
    print "Range from",RANGE_START,"to",RANGE_END
    # Generate the random number
    random_number = random.randint(RANGE_START, RANGE_END)
    # Give the user a certain amount of guesses
    for i in range(1, NUMBER_OF_GUESSES + 1):
        guess = int( raw_input('Guess the number: ') )
        if guess == random_number:
            print "Well done!!!"
            break
        elif guess > random_number:
            print "Too high"
            if i != NUMBER_OF_GUESSES:
                print "You have",NUMBER_OF_GUESSES - i, "guesses left"
        else:
            print "Too low"
            if i != NUMBER_OF_GUESSES:
                print "You have",NUMBER_OF_GUESSES - i, "guesses left"

    if guess != random_number:
        print "Sorry, you've had all your guesses, let's try a new number."
