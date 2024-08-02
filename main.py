def print_board(board: List[List[str]]) -> None:
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # فقط بین ردیف‌ها خط رسم شود
            print("-" * 9)

def check_winner(board: List[List[str]], player: str) -> bool:
    # بررسی سطرها
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # بررسی ستون‌ها
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # بررسی قطرها
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def get_valid_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1, 2]:
                return value
            else:
                print("Please enter a number between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe() -> None:
    board: List[List[str]] = [[" " for _ in range(3)] for _ in range(3)]
    current_player: str = "X"
    for _ in range(9):
        print_board(board)
        row: int = get_valid_input(f"Player {current_player}, enter the row (0, 1, 2): ")
        col: int = get_valid_input(f"Player {current_player}, enter the column (0, 1, 2): ")
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell is already taken. Try again.")
    print_board(board)
    print("It's a tie!")

tic_tac_toe()

