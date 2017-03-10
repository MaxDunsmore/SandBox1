"""
Ask user to input name then print every other letter.

oddName. Created by Max, March 2017
"""
name = 0
valid_input = False
while not valid_input:
    name = str(input("Please Enter ur name"))
    if len(name) <= 0:
        valid_input = False
    else:
        valid_input = True
print(name[::2])
