                #SELF ATTEMPT

# import random

# def main():
#     logos()
#     guess_mech()


# def logos():
#     print("###### WELCOME TO THE NUMBER GUESSING GAME ######")
#     print("------ Enter a number between 1 and 100 ------")

# def guess_mech():
#     number = random.randint(1, 100)
#     guess_counter = 1
        
#     while guess_counter <= 7:
#         player_guess = int(input(f"Attempts: {guess_counter}/7 Enter Your Guess: "))
            
#         if player_guess > number:
#             print("Too High! Try a lower number.")
#         elif player_guess < number:
#             print("Too Low! Try a higher number.")
#         elif player_guess == number:
#             print(f"BINGO!! THE NUMBER WAS {number}!!")
#             print(f"You guessed it in {guess_counter} attempts!")
#             break

#         guess_counter += 1
    
#     print(f"YOUR LOST! THE NUMBER WAS {number}")


# main()




                #IMPROVED AND EFFICIENT VERSION

import random


def main():
    logos()
    guess_mech()


def logos():
    print("###### WELCOME TO THE NUMBER GUESSING GAME ######")
    print("------ Enter a number between 1 and 100 ------")


def guess_mech():
    number = random.randint(1, 100)
    max_attempts = 7
    guess_counter = 1
    has_won = False

    while guess_counter <= max_attempts:
        try:
            player_guess = int(input(f"Attempts: {guess_counter}/{max_attempts} | Enter your guess: "))
        except ValueError:
            print("Enter a valid integer!!")
            continue

        if player_guess > number:
            print("Too High! Try a lower number!")
        elif player_guess < number:
            print("Too Low! Try a higher number!")
        else:
            print(f"BINGO!! THE NUMEBR WAS {number}!!")
            print(f"You guessed it in {guess_counter} attempts!")
            has_won = True
            break

        guess_counter += 1

    if not has_won:
        print(f"YOU LOSE!! THE NUMBER WAS {number}")


if __name__ == "__main__":
    main()
