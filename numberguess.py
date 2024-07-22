import random

def test():
    comp_choice = random.randint(0,10)

    player_choice = int(input("Welcome to the Number Guessing Game! Please choose a whole number in the range of 0 and 10\n"))

    while True:
     if 0 <= player_choice <= 10:
            break
     else:
        print("Chosen value in not in the given range")
        player_choice = int(input("Welcome to the Number Guessing Game! Please choose a whole number in the range of 0 and 10\n"))
    
    print(f"Your choice is {player_choice}!")
    print(f"The computer chose {comp_choice}!")

    if player_choice == comp_choice:
        print("You win!")
    else:
        print("You Lose!")
    

test()