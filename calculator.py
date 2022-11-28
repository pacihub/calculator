import os

# operator functions definition
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# dict with operations symbols as keys and function names as values
opns = {
    '+' : add,
    '-' : sub,
    '*' : multiply,
    '/' : divide
}

# flag used to decide if calculation result is used for further calculating
use_last_rezult = False
rezult = None

# check if previous result will be used for further calculation. if yes, then n1 = previous result
while True:
    if use_last_rezult == False:        # not gonna use previous result. Will prompt user for new n1
        # prompt for first number and check for valid input
        while True:
            try:
                n1 = float(input("First number: "))
            except ValueError:
                print('You have to type a number.')
            else:
                break

    else:       # gonna use previous result so automatically assigning rezult to n1
        n1 = rezult
        print(f"the first number is {rezult}")

    # prompt for mathematical operation and check for valid input
    while True:
        try:
            operation = input("pick an operation ( +, -, *, / ):  ")
            if operation not in opns.keys():
                raise ValueError('pick an operation')
            else:
                break
        except:
            pass


    # prompt for second number and check for valid input
    while True:
        try:
            n2 = float(input("Second number: "))
        except ValueError:
            print('You have to type a number.')
        else:
            break

    # compares user input to a key in 'opns' dictionary and invokes the corresponding function with user's
    # inputs for n1 and n2
    for i in opns.keys():
        if i == operation:
            rezult = opns[i](n1,n2)

    print(f"{n1} {operation} {n2} = {rezult}")

    # options for prompting whether or not the user wants to use the current result
    yes_options = ['y', 'yes', 'yeah', 'yiesh']
    no_options = ['n', 'no', 'nope', 'nopers']

    # prompt user if they want to use the current result for further calculation
    while True:
        try:
            cont = input("Type 'y' to use that number, and 'n' to start over ")

            if cont in no_options:
                use_last_rezult = False
                os.system('clear')      # clear screen and start over
                break
            elif cont in yes_options:
                use_last_rezult = True
                break
        except:
            pass

