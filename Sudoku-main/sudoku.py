import random

def print_board(board):
    """Helper function to print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty(board):
    """Find an empty space in the board (represented by 0)."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(board, num, pos):
    """Check if a number is valid in a given position."""
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    """Solve the Sudoku board using backtracking."""
    find = find_empty(board)
    if not find:
        return True  # Solved
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Reset if not valid

    return False

def generate_board():
    """Generate a new Sudoku board with a unique solution."""
    board = [[0]*9 for _ in range(9)]
    for _ in range(17):  # Fill 17 cells randomly to ensure a unique solution
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_valid(board, num, (row, col)) or board[row][col] != 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        board[row][col] = num
    solve(board)  # Solve the board to make sure it's valid
    for _ in range(45):  # Remove some numbers to create the puzzle
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board

def main():
    board = generate_board()
    print("Welcome to Sudoku!")
    print_board(board)

    while True:
        print("\nEnter your move in the format 'row col num' (e.g., '1 1 5') or 'q' to quit:")
        move = input()
        if move.lower() == 'q':
            print("Thanks for playing!")
            break
        try:
            row, col, num = map(int, move.split())
            if row < 1 or row > 9 or col < 1 or col > 9 or num < 1 or num > 9:
                print("Invalid input. Rows, columns, and numbers must be between 1 and 9.")
                continue
            row -= 1
            col -= 1
            if board[row][col] != 0:
                print("This cell is already filled.")
                continue
            if is_valid(board, num, (row, col)):
                board[row][col] = num
                print_board(board)
                if not find_empty(board):
                    print("Congratulations, you solved the Sudoku!")
                    break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter the move in the correct format.")

if __name__ == "__main__":
    main()
