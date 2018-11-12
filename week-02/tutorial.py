# If statements check if what's between the parentheses is true.
# If what is between the parentheses is true, it does whatever is in the
# "block" of code beneath it.
if(100 > 10):
    print("100 is greater than 10.")
    print("This line is part of the \"block\" that gets read if 100 > 10")
print("This line isn't part of the block of code.")

# There are also else statements which get used if what's in the parentheses
# of the if statement is false.
if(2 < 1):
    print("This line won't be printed since 2 is more than 1.")
else:
    print("This is printed since 1 is less than 2.")
print("This will be printed no matter what.")

# Here is a list of useful stuff you can do to compare things in if statements.
# These are called conditional statements.
# a > b     Returns true if a is more than b
# a < b     Returns true is a is less than b
# a >= b    Returns true if a is greater than or equal to b
# a <= b    Returns true if a is less than or equal to b
# a != b    Returns true is a doesn't equal b
# a == b    Returns true is a equals b

# You can also use elif statements, which stands for else if.
# You can use them like this.
print("Type in a number equal to or greater than 0.")
mysteryNumber = int(input())
if(mysteryNumber > 10):
    print("The number you entered is greater than 10.")
elif(mysteryNumber < 10):
    print("The number you entered is less than 10.")
else:
    print("The number isn't greater or less than 10, so it is 10.")

# You can put if statements inside of each other, as well.
if(mysteryNumber < 10):
    if(mysteryNumber < 5):
        print("The number is between 0 and 4")
    elif(mysteryNumber > 5):
        print("The number is between 6 and 9")
    else:
        print("The number is 5")

# Lists are something that hold a bunch of variables that don't have
# to be the same type. You make them by listing variables separated
# by commas
exampleList = ['Riley', 420, 3.14, True, "See? Lists can hold anything."]

# The way you refer to an item in a list is by using something called
# an index number. The first item always has the index number of 0.
print(exampleList[0])  # This will print Riley
print(exampleList[1])  # This will print 420
print(exampleList[3])  # This will print True
exampleList[1] += 5  # This would add 5 to 420, so [1] would be 425

# A for loop executes block below it for as many items as there are
# in the list you give it. This loop prints out everything in exampleList.
for exampleItem in exampleList:
    print(exampleItem)

# The way it works is by creating a variable named whatever comes after
# the word for. In this case the variable is named exampleItem. Then,
# it gives that variable the value of the first item in exampleList,
# which would be Riley, and does whatever is in the block of code below
# it. When it gets done with that, it assigns the next item in the list
# to exampleItem and does the block of code again. This keeps going until
# it loops through every item in exampleList.

# Even though they aren't lists, strings work the same way. This example
# goes through every letter in the sentence I give it and makes them
# uppercase.
newString = ""  # Since newString doesn't exist yet, I have to make it.
for letter in "saturdays are for the boyz":
    newString += letter.upper()  # letter.upper() makes it uppercase.
print(newString)
