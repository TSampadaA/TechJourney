To catch a specific exception, you will need to know the exact exception that is thrown. 
You can find this out by googling or experimenting. To catch all exceptions, just do an except. 
#Some examples of exceptions: https://www.w3schools.com/python/python_ref_exceptions.asp

try:
    number = int(input("What is your favorite number? \n"))
    print("Your favorite number times 6 is " + str(number * 6))
except:
    print("You didn't give me a number, did you?")


#exception with an error message
except <type of exception> as error:
    print(error)
