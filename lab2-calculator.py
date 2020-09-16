###### STILL NEEDS COMMENTS ######

## PROBLEM 2: Displaying the Current Value

def display_current_value():
    print("Current Value:", current_value)

## PROBLEM 3: Addition

def add(to_add):
    global current_value

    log_history()
    current_value += to_add


## PROBLEM 4: global
#NOT FINISHED

# If its not declared as a global variable, you get an error :
# UnboundLocalError: local variable 'current_value' referenced before assignment

"""
#### NOT FINISHED ####
Understanding what the global declaration does is understanding how scope
works in python. By default when defining a variable within a function block

Eg.
--------------------------
def foo():
    new_var = 5
    print(new_var)
    new_var += 1
    print(new_var)

print(new_var)

--------------------------
"""

## PROBLEM 5: Multiplication and Division

def multiply(scalar):
    global current_value

    log_history()
    current_value *= scalar

def divide(denom):
    try:
        multiply(1/denom)
    except ZeroDivisionError:
        print("MATH ERROR: Division by zero")

## PROBLEM 6: Memory and Recall

def to_memory():
    global current_value, memory
    memory = current_value

def recall():
    global current_value, memory
    log_history()
    current_value = memory

## PROBLEM 7: Undo

def log_history():
    global current_value, previous_value
    previous_value = current_value

def undo():
    global current_value, previous_value
    temp = current_value
    current_value = previous_value
    previous_value = temp

## PROBLEM 1: Welcome message

current_value = 0
previous_value = 0
memory = 0


if __name__ == "__main__":
    print("Welcome to the calculator program.")
    print("Current Value:", current_value)

    # Test for Problem 2:
    display_current_value()

    # Test for Problem 3:
    add(5)
    display_current_value()

    # Test for Problem 5:
    multiply(5)
    display_current_value()
    divide(5)
    display_current_value()
    divide(0)
    display_current_value()
    multiply(3)
    display_current_value()
    undo()
    display_current_value()
    undo()
    to_memory()
    add(1)
    display_current_value()
    divide(4)
    display_current_value()
    recall()
    display_current_value()

