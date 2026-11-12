# import random



# def main():
#     statements()
#     mechanism()



# def statements():
#     user_name = input("Hello! What is your name?")
#     print("--- NUMBER GUESSING GAME ---")
#     print(f"Welcome!! {user_name}")



# def mechanism():
#     guess_attempts = 1
#     max_attempts = 7
#     winning = False
#     random_guess = random.randint(1, 100)
    
#     while guess_attempts <= max_attempts:

#         user_guess = int(input(f"Attempt:{guess_attempts}/{max_attempts} | Guess: "))

#         if random_guess > user_guess:
#             print("Too Low!")
#         elif random_guess < user_guess:
#             print("Too High!")
#         else:
#             print(f"YOU WIN! The number is: {random_guess}")
#             winning = True
#             break

#         guess_attempts += 1

#     if not winning:
#         print(f"YOU LOST! The number was: {random_guess}")



# if __name__ == "__main__":
#     main()



                #MAKING THE COMPUTER GUESS THE NUMBER BETWEEN 1 AND 100

import random



def main():
    guess(100)



def guess(x):

    computer_won = False
    guess_attempts = 1
    max_attempts = 7
    low = 1
    high = x

    while guess_attempts <= max_attempts:

        #making sure the high and low is not the same
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low    #can also be high as they will be the same

        print(f"Attempts: {guess_attempts}/{max_attempts} | Guess: {computer_guess}")
        user_feedback = input("High (H), Low (L) or Correct (C)").capitalize()

        if user_feedback == 'H':
            high = computer_guess - 1
        elif user_feedback == 'L':
            low = computer_guess + 1
        elif user_feedback == 'C':
            print("BINGO! I WON!!")
            computer_won = True
            break

        guess_attempts += 1

    if not computer_won:
        print("OH NO! I LOST!")

            

if __name__ == "__main__":
    main()