import random

my_number = random.randint(0, 100)
count = 0


def is_notnum(input_string):
    i = 0
    for item in range(len(input_string)):
        char_ascii = ord(input_string[i])
        if char_ascii > 58 or char_ascii <48:
            if char_ascii == 46:
                return True
        elif char_ascii > 58 or char_ascii <48:
            if i != 0 and char_ascii !=45:
                return True
        elif len(input_string) == 1:
            if char_ascii > 57 or char_ascii < 48:
                return True
        i += 1
    return False
        

def check_guess(guess, count):
    guess_num = int(guess)
    if guess_num > my_number:
        print "That's too high.  Guess again."
        return False
    elif guess_num < my_number:
        print "That's too low.  Try again."
        return False
    else: 
        print "Hell yeah. You're so good at guessing! Good thing I only had to help you %s times." % count
        return True
    count += 1 

    

def guessing_game():
    print "What is your name?"
    name = raw_input()
    print "%s, I'm thinking of a number between 1 and 100. Try to guess the number." % name

    count = 0
    success = False
    while success == False: 
        input_string = raw_input("Guess a number: ")
        if is_notnum(input_string):
            print "Try again with a whole number!"
        else: 
            success = check_guess(input_string, count)
        count += 1

guessing_game()