To catch a specific exception, you will need to know the exact exception that is thrown. You can find this out by googling or experimenting. To catch all exceptions, just do an except. 

try:
    number = int(input("What is your favorite number? \n"))
    print("Your favorite number times 6 is " + str(number * 6))
except:
    print("You didn't give me a number, did you?")
