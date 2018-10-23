# This is a comment. You make comments by typing a "#" at the start
# of a line. They're useful for explaing your code to other people.

# This is a variable. You define them like this:
a = 5

# You can name them anything except for stuff that's already taken.
myAge = 18

# There are differnt types of data a variable can hold.
# myAge is holding an integer, which is a whole number.

# Another type is strings, which consist of characters.
# There are three ways to define strings:
myFirstName = "Riley"
myMiddleName = 'Griffin'
myLastName = '''Guy'''

# Floats are numbers with a decimal value.
pi = 3.14

# Boolean values can hold True or False values.
# True represents 1, False represents 0.
thisVariableIsTrue = True
thisVariableIsAlsoTrue = 1
thisVariableIsFalse = False
thisVariableIsAlsoFalse = 0

# You can assign variables to other variables.
a = 5
b = a

# You can add stuff to variables.

# This adds 1 to a.
a = a + 1

# This is a quicker way of doing the same thing.
a += 1

# You can add stuff to strings, too.
myFullName = myFirstName + ' ' + myMiddleName + ' ' + myLastName
myFirstName = myFirstName + ' is cool.'

# To output stuff to the terminal, use the print function.
# This line will output my name to the terminal.
print(myFullName)

# It doesn't have to be a string, either.
# You can print other data types too, like floats.
print(pi)

# You can also get input from the user with the raw_input function.
print("Type something")
userInput = input()
print("You typed in: " + userInput)

# You could have done the same thing like this:
print("Riley is the " + input() + " club president ever.")
