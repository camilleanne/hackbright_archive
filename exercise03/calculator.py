import arithmetic

def instructions():
    print """
    This calculator is limited to: 
    add (+), subtract (-), multiply (*), divide (/), 
    square (square), cube (cube), power (pow), modulus (mod).
    Please use the operator first, e.g. '+ 2 3'.
    This calculator cannot take more than 2 inputs, some
    tasks only require one. 

    To quit, type 'q'. 

    To see these instructions again, type 'instructions.'
    """

def main():

    instructions()

    while True:
        math_input = raw_input("> ") # get math input from user

        tokens = math_input.split(" ") # split math instructions at space

        if tokens[0] == "+":
            if len(tokens) != 3:
                print "Please use the format '+ 2 3'"
            else:
                print arithmetic.add(int(tokens[1]), int(tokens[2]))
        
        elif tokens[0] == "-":
            if len(tokens) != 3:
                print "Please use the format '- 2 3'"
            else:    
                print arithmetic.subtract(int(tokens[1]), int(tokens[2]))
        
        elif tokens[0] == "*":
            if len(tokens) != 3:
                print "Please use the format '* 2 3'"
            else:            
                print arithmetic.multiply(int(tokens[1]), int(tokens[2]))

        elif tokens[0] == "/":
            if len(tokens) == 3 and tokens[2] == "0":
                print "You cannot divide by zero! Try again."
            elif len(tokens) < 3:
                print "Please use the format '/ 2 3'"
            else:
                print arithmetic.divide(tokens[1], tokens[2])

        elif tokens[0] == "square":
            if len(tokens) > 2:
                print "Please use the format 'square 2'"
            else:
                print arithmetic.square(int(tokens[1]))

        elif tokens[0] == "cube":
            if len(tokens) > 2:
                print "Please use the format 'cube 3'"
            else:
                print arithmetic.cube(int(tokens[1]))

        elif tokens[0] == "pow":
            if len(tokens) != 3:
                print "Please use the format 'pow 2 3'"
            else:
                print arithmetic.power(int(tokens[1]), int(tokens[2]))
    
        elif tokens[0] == "mod":
            if len(tokens) == 3 and tokens[2] == "0":
                print "You cannot divide by zero! Try again."
            elif len(tokens) < 3:
                print "Please use the format 'mod 2 3'"
            else:            
                print arithmetic.mod(int(tokens[1]), int(tokens[2]))

        elif len(tokens) > 3:
            print "Please try again with 2 numbers"

        elif tokens[0] == "instructions":
            instructions()

        elif tokens[0] == "q":
            return False

        else:
            print "Please try again. Confused? Try typing 'instructions.'"



main()