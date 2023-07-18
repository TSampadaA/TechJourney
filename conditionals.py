color = str(input("What is your favorite color?\n"))

if (color == "red" or color == "pink"):
    print("The color is red or pink.")
else:
    print("The color is not red or pink.")



color = str(input("What is your favorite color?\n"))
color = color.lower() # <- this is different from previous step

if (color == "red" or color == "pink"):
    print("The color is red or pink.")
elif (color != "orange"):
    print("The color is not red, pink, or orange. It is " + color + ".")
else:
    print("Ahah! So it is orange.")



