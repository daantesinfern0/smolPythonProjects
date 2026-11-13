                #SELF ATTEMPT (with some doc help)

import random



def main():
    mechanism()



def mechanism():
    
    user_win = 0
    computer_win = 0

    choices = ['Rock', 'Paper', 'Scissors']

    # loop until either player reaches 2 wins
    while user_win < 2 and computer_win < 2:

        computer_choice = random.choice(choices)
        user_choice = input("Choose betwee Rock | Paper | Scissors: ").strip().capitalize()

        # making sure only relevant answer are entered
        if user_choice not in choices:
            print("Invalid choice! The options are Rock, Papers, or Scissors")
            continue

        print(f"Computer chose: {computer_choice}")

        # three scenrious are possible while palying the game
        if user_choice == computer_choice:
            print("It is a tie!")
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            print(f"{user_choice} beats {computer_choice}! | Point for You!")
            user_win += 1
        else:
            print(f"{computer_choice} beats {user_choice}! | Point for PC!")
            computer_win += 1


    # announcing the winner after the loops ends
    if computer_win > user_win:
        print(f"Computer won the match with {computer_win} points!")
    else:
        print(f"You won the match with {user_win} points!")

      

if __name__ == "__main__":
    main()