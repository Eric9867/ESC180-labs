## PROBLEM 1: Your first Python programc

# The code below prints "Hello, Python" to the shell followed
# by a blank line as to make the shell look more organized.

print("Hello, Python\n")

## PROBLEM 2: Greetings

# The 2 lines of code below essentially do
# the same thing that happened in problem 1.
print("Hello, Halil Kelebek")
print("Hello, Eric Lefort\n")

## PROBLEM 3: Variables

# As to not have to continuously type out the names "Halil Kelebek"
# & "Eric Lefort" in the print statement below, the names are stored
# in vars name1 and name2.
# This way, if we wanted to alter the names in our print statement below,
# we would only need to alter the names stored in the var instead of each
# instance of the name in the print statement.
name1 = "Halil Kelebek"
name2 = "Eric Lefort"

# Vars name1 and name2 are called in the print statement below
print("Hello, " + name1 + " and " + name2 + ". Your names are "
     + name2 + " and " + name1 + ". Hi there. Your names are still "
     + name1 + " and " + name2 + ".\n")

## PROBLEM 4: Tracing

# When tracing we can view when the name variables get
# altered through the workspace tool below the shell
name1 = "Prof. Cluett"
name2 = "Prof. Thywissen"

## PROBLEM 5: More greetings

# This line asks the user for a name and stores the user input in the name variable
name = input("What is your name? ")

# the conditional below checks if name is Lord Voldemort.
# The .lower() function is used to remove the case sensitivity.
if name.lower() == "lord voldemort":
    print("I'm not talking to you.")
else:
    print("Hello, " + name)