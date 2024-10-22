import random

def initialize_board_from_input(N):
    """Initializes the N-Queens board based on user input for each queen's position in each row."""
    board = []
    print(f"Enter the column position for each queen in each row (0 to {N-1}):")
    for i in range(N):
        col = int(input(f"Row {i}: "))  # Ask the user for each queen's column position
        while col < 0 or col >= N:
            print(f"Invalid input. Please enter a column value between 0 and {N-1}.")
            col = int(input(f"Row {i}: "))  # Re-prompt if input is invalid
        board.append(col)
    return board

def calculate_conflicts(board):
    """Calculates the number of conflicts (attacking queens) on the current board."""
    conflicts = 0
    N = len(board)
    
    for i in range(N):
        for j in range(i+1, N):
            # Queens in the same column or diagonal are in conflict
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def generate_neighbors(board):
    """Generates all neighbors by moving each queen within its row to different columns."""
    N = len(board)
    neighbors = []
    
    for row in range(N):
        for col in range(N):
            if col != board[row]:  # Only consider new positions for the queen
                neighbor = board[:]
                neighbor[row] = col  # Move queen to a new column
                neighbors.append(neighbor)
                
    return neighbors

def print_board(board):
    """Prints the board in a readable format."""
    N = len(board)
    for row in range(N):
        line = ['.'] * N
        line[board[row]] = 'Q'
        print(' '.join(line))
    print("\n")

def hill_climbing(N, initial_board):
    """Performs Hill Climbing search for the N-Queens problem starting from an initial board."""
    # Step 1: Start with the user-provided initial board
    current_board = initial_board
    current_conflicts = calculate_conflicts(current_board)
    
    print(f"Initial board with heuristic {current_conflicts}:")
    print_board(current_board)
    
    steps = 0
    
    while True:
        steps += 1
        # Step 2: If no conflicts, solution found
        if current_conflicts == 0:
            print(f"Solution found in {steps} steps!")
            return current_board
        
        # Step 3: Generate all neighbors
        neighbors = generate_neighbors(current_board)
        best_neighbor = None
        best_neighbor_conflicts = current_conflicts
        
        # Step 4: Evaluate neighbors and select the best one
        for neighbor in neighbors:
            neighbor_conflicts = calculate_conflicts(neighbor)
            if neighbor_conflicts < best_neighbor_conflicts:
                best_neighbor = neighbor
                best_neighbor_conflicts = neighbor_conflicts
        
        # Step 5: If no better neighbor, return the current board (local maximum or solution)
        if best_neighbor_conflicts >= current_conflicts:
            print(f"Local maximum reached with heuristic {current_conflicts}:")
            print_board(current_board)
            return current_board
        
        # Step 6: Move to the best neighbor
        current_board = best_neighbor
        current_conflicts = best_neighbor_conflicts
        
        print(f"Step {steps} with heuristic {current_conflicts}:")
        print_board(current_board)

# Get user input for N
N = int(input("Enter the value of N for the N-Queens problem: "))

# Get user input for the initial board configuration
initial_board = initialize_board_from_input(N)

# Run the hill climbing algorithm with the user-provided initial board
solution = hill_climbing(N, initial_board)
