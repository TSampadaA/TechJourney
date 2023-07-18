dogBreeds = ["poodle", "mastiff", "great dane"]

breed = str(input("What is your favorite kind of dog?\n"))
breed = breed.lower()

if (breed not in dogBreeds):
    print("Hmm... I'm not familiar with that kind of dog.")
elif (breed == dogBreeds[0]):
    print("That's my favorite dog too!")
else:
    print("Nice.")
