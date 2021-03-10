#######################################################################
#Name: Luke Parks
#Date: 02/28/2021
#Description: Creating an exciting "Choose your own adventure" story!
#######################################################################
print("Welcome to my story! Any choice you make takes you down a different path!")
print()
print("To select choices, just type the number of the choice and hit the enter key.")
print()
print("And now, let's begin your story!")
print()
def fxn_option():
    return input("Please select your answer as one of the numbers.")
def fxn_part1():
    print("Hello, young traveler. What brings you to this island? Surely you could not have come here without purpose.")
    print()
    print("What do you say for yourself?")
    print()
    print("(1) I'd like to ask a question instead: where am I?")
    print("(2) I'm... not sure. I don't remember.")
    print()
    option = fxn_option()
    if option == "1":
        print("Aren't you an impatient one? I guess it can't be helped.")
        print("Welcome to the Island of Black Sands.")
    elif option == "2":
        print("Hm. Puzzling indeed.")
        print("Welcome to the Island of Black Sands.")
    else:
        print("Invalid input.")
        print()
        fxn_option()
part1 = fxn_part1()
