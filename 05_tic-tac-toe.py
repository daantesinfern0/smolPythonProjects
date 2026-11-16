def play_game():
  board = [" " for _ in range(9)]
  current_player = "X"

  def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

  def check_winner(player):
    win_conditions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    return any(
        board[a] == board[b] == board[c] == player for a, b, c in win_conditions
    )

  print("Welcome to Tic-Tac-Toe! Positions are numbered 1 to 9, left to right.")

  while True:
    print_board()

    # Get valid player input
    while True:
      try:
        move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
        if 0 <= move <= 8 and board[move] == " ":
          board[move] = current_player
          break
        print("Spot taken or out of range. Try again.")
      except ValueError:
        print("Invalid input. Enter a number from 1 to 9.")

    # Check end-game conditions
    if check_winner(current_player):
      print_board()
      print(f"Player {current_player} wins!")
      break

    if " " not in board:
      print_board()
      print("It's a tie!")
      break

    # Switch turns
    current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
  play_game()
