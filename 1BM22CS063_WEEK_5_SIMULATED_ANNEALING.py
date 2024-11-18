import random
import math

def calculate_conflicts(board):
    """
    Calculate the number of conflicts in the board configuration.
    """
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def simulated_annealing(n, initial_board):
    """
    Solve the N-Queens problem using simulated annealing.
    """
    # Start with the user-provided initial board
    current_board = initial_board[:]
    current_conflicts = calculate_conflicts(current_board)
    temperature = 1000
    cooling_rate = 0.99
    iterations = 10000

    for _ in range(iterations):
        if current_conflicts == 0:
            return current_board  # Solution found

        # Randomly choose a queen to move
        row = random.randint(0, n - 1)
        new_board = current_board[:]
        new_position = random.randint(0, n - 1)
        while new_position == current_board[row]:  # Ensure a different position
            new_position = random.randint(0, n - 1)

        new_board[row] = new_position
        new_conflicts = calculate_conflicts(new_board)

        # Accept the move with probability based on temperature
        delta_conflicts = new_conflicts - current_conflicts
        if delta_conflicts < 0 or random.random() < math.exp(-delta_conflicts / temperature):
            current_board = new_board
            current_conflicts = new_conflicts

        # Cool down the system
        temperature *= cooling_rate

    # If no solution is found, return the current best
    return None

def main():
    print("Simulated Annealing for N-Queens Problem")
    n = int(input("Enter the number of queens (N): "))
    initial_board = []

    print("Provide the initial positions of queens (row index for each column):")
    for i in range(n):
        position = int(input(f"Column {i+1}: "))
        if 0 <= position < n:
            initial_board.append(position)
        else:
            print("Invalid position. Please enter a value between 0 and N-1.")
            return

    solution = simulated_annealing(n, initial_board)
    if solution:
        print("Solution found:")
        for col, row in enumerate(solution):
            print(f"Queen at column {col+1}, row {row}")
    else:
        print("No solution found within the iteration limit.")

if __name__ == "__main__":
    main()
