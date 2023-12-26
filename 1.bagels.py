import random

def bagels(total_guesses=10):
    
    TOTAL_GEUSSES = total_guesses
    
    opening_text  = f""" 
    I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
    I have thought up a number.
    You have {TOTAL_GEUSSES} guess/es to get it.

    """
    number = str(random.randint(100, 999))
    number_lst = [i for i in number]

    print(opening_text)

    correct = False
    i = 1
    while not correct:

        if i > TOTAL_GEUSSES:
            print("You ran out of guesses. The answer was {}".format(number))
            break
        
        guess = input("Guess #{}: ".format(i))
        
        if guess.isnumeric() == False or len(guess) != 3:
            print("Please enter a number with 3 digits.")
            continue
        
        if guess == number:
            print("You got it! the number was {}".format(number))
            correct = True
        
        clue = []
        for index in range(len(guess)):
            if guess[index] == number[index]:
                clue.append("Fermi")
            elif guess[index] in number_lst:
                clue.append("Pico")
        if len(clue) == 0:
            print("Bagels")
            
        else:
            random.shuffle(clue)
            print(" ".join(clue))     
            
        i += 1
        
    play_again = input("Do you want to play again? (yes or no) ")
    if play_again.lower().startswith("y"):
        bagels()
    else:
        print("Bye!")

if __name__ == "__main__":
    bagels()