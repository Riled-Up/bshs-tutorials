# There are multiple ways to do this correctly, this is just the example
# I wrote.

oldSong = input()
newSong = ""
for letter in oldSong.upper():
    if(letter == 'B'):
        newSong += '13'
    elif(letter == 'I'):
        newSong += '1'
    elif(letter == 'S'):
        newSong += 'Z'
    else:
        newSong += letter
print(newSong)
