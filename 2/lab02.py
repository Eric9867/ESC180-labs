###### STILL NEEDS COMMENTS ######

## PROBLEM 2: Displaying the Current Value

def display_current_value():
    print("Current Value:", current_value)

## PROBLEM 3: Addition

# Sets the global variable current_value equal to itself + the function input variable to_add
def add(to_add):
    global current_value

    log_history()
    current_value += to_add


## PROBLEM 4: global

"""
Understanding what the global declaration does is understanding how scope
works in python.
By default when defining a variable within a function block that variable only exists within the function block. So for example we couldnt just call the to_add variable in the add(to_add) function outside of the function block. Another example is given below:

Eg.
--------------------------
new_var = 0
print(new_var)

def foo():
    new_var = 5
    print(new_var)
    new_var += 1
    print(new_var)

foo()
print(new_var) <-- this print statement will just print 0 since the foo() only changes the 'new_var' within
                   the function block.

--------------------------

Declaring a variable as global within a function gets over this problem. when we specify a variable as global the variable within the function block will this time be referring to the variable with the same name outside of the function block:

Eg.
--------------------------
new_var = 0
print(new_var)

def foo():
    global new_var

    new_var = 5
    print(new_var)
    new_var += 1
    print(new_var)

foo()
print(new_var) <-- this print statement will now print 6 since 'new_var' has now been declared as a global
                   var in foo so whatever happens to new_var within the function block will happen to the
                   new_var outside of the block since they are now referring to the same variable.

--------------------------
"""

## PROBLEM 5: Multiplication and Division

# Sets the global variable current_value equal to itself times the input
# number given by the variable name scalar.
def multiply(scalar):
    global current_value

    log_history()
    current_value *= scalar

# for any numerical input denom other than denom = 0, the divide function calls
# the multiply function using  the reciprocal of the denom input as the new input.
# A try except statement was used to catch a ZeroDivisionError incase denom = 0,
# in which case a message is printed.
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

