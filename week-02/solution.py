# There are multiple ways to do this correctly, this is just the example
# I wrote.

oldSong = input()  # Get input from user
oldSong = oldSong.upper()  # Capitalize everything
newSong = ""  # Create a new blank string
for letter in oldSong.upper():  # Go through every letter in oldSong
    if(letter == 'B'):  # Add '13' to newSong if the letter is 'B'
        newSong += '13'
    elif(letter == 'I'):  # Add '1' if it's 'I'
        newSong += '1'
    elif(letter == 'S'):  # Add 'Z' if it's 'S'
        newSong += 'Z'
    else:  # Since it wasn't those, we don't change it before adding it.
        newSong += letter 
print(newSong)  # Once every letter has been gone through we print it
