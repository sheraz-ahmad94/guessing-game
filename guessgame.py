import random


#Generates a Random Number Between 1 to 100 and then Loops That Many Times to Generate Another Random Number
def gen_ran():
    n = random.randint(1, 100)
    for x in range(n):
        number = random.randint(1, 100)
    return number

#User Guess Game Function
def user_guess():
    number = gen_ran() #Generates a Random Number
    guess = int(input ("Guess the Number (1 - 100): "))

    #Loop Runs Until the User has Guessed the Number. Hints are Given if the Number to Guess is Lower or Higher
    while guess != number:
        
        if guess < number:
            print(f"Wrong!! Number is Greater Than {guess}")
        elif guess > number:
            print(f"Wrong!! Number is Lesser Than {guess}")

        guess = int(input ("Guess the Number (1 - 100): "))
    
    print(f"{number} is Correct!!")

#Utility Funtion for Computer Guess Game. Moves the Number Towards Half of the Range
def trav(x,y):
    number = int((x+y)/2)
    return number

#Computer Guess Game Function
def comp_guess():
    low = 1
    high = 100

    feedback = "" #Feedback from User if Number to Guess is Lower or Higher

    number = gen_ran() #Starts by Generating a Wild Guess Between 1 and 100

    print(f"Is the Number {number}?")
    feedback = input("Type L for Low, H for High or Y If It Is Correct: ").capitalize()

    #Loop Until the Number is Found
    while feedback != 'Y':
        if feedback == 'L':
            high = number - 1
            number = trav(low, high)
        elif feedback == 'H':
            low = number + 1
            number = trav(low, high)
        
        print(f"Is the Number {number}?")
        feedback = input("Type L for Low, H for High or Y If It Is Correct: ").capitalize()

while True:
    print("--- MENU ---")
    print("1 - User Guessing Game")
    print("2 - Computer Guessing Game")
    print("3 - Exit")
    choice = int(input("Select: "))

    if choice == 1:
        user_guess()
    elif choice == 2:
        comp_guess()
    elif choice == 3:
        exit()
    else:
        print("Wrong Choice")