# How to print from a File
# In Terminal app run either
# touch helloworld.py # creates it with empty contents or
# code hellowworld.py
# HelloWorld.py >> New File

# Add this code and save the file
print(“Hello, World”)

# Click Debug menu, then "Run without debugging" or
# Click ▶ icon above the file

# Jokes: print(), input()
# Write a joke or two using print() and input().. 

print("Why was the computer late to work?")
print("It had a harddrive!")

# How to get input from a user
print("What is your name?")
input()
print("Nice to meet you!")

# Inputs can print too
input("What is your name?")
print("Nice to meet you!")

# Newline character
input("What is your name?\n")
print("Nice to meet you!")

# How to get string input from a user, store it within a variable, and print it back to the user
name = input("What is your name?\n")
print("Nice to meet you, “ + name + “!")

# How to get numerical input from a user, store it within a variable, and print it back to the user
birthYear = input("What year were you born?\n");
yearsAgo = 2022 - birthYear;
print("You were born about " + yearsAgo + " years ago");

birthYear = input("What year were you born?\n");
yearsAgo = 2022 - int(birthYea)r;
print("You were born about " + yearsAgo + " years ago");


birthYear = input("What year were you born?\n");
yearsAgo = str(2022 - int(birthYear));
print("You were born about " + yearsAgo + " years ago");
