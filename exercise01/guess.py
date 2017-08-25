import random

def guessing_game():
    print "Hey there, guessypants! What's your name?"
    name = raw_input()
    print "Hi %s. I'm thinking of a number between 1 and 100. Try to guess the number." % name

    prompt = 'Your guess? '
    guess = 0

    number = random.randint(1, 100)

    while guess != number:
        try:
            guess = int(raw_input(prompt))
            if guess < number:
                print "Your guess is too low."
                #guess = int(raw_input(prompt))
                
            if guess > number:
                print "Your guess is too high."
                #guess = int(raw_input(prompt))
        
            if guess == number:
                print "Congratulations, you're right %s!" % name

        except ValueError:
            print "Try again, with a whole number!"
            
guessing_game()