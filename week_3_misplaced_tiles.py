import heapq

# Function to get the index of the empty tile (represented as 0)
def get_empty_tile_position(state):
    return state.index(0)

# Function to calculate the number of misplaced tiles (heuristic)
def misplaced_tiles(state, goal):
    return sum([1 if state[i] != goal[i] and state[i] != 0 else 0 for i in range(9)])

# Function to generate the possible next states
def get_neighbors(state):
    neighbors = []
    empty_tile_index = get_empty_tile_position(state)
    
    # Mapping index to coordinates on 3x3 grid
    x, y = divmod(empty_tile_index, 3)
    
    # Possible moves (up, down, left, right)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < 3 and 0 <= ny < 3:  # Ensure move is within bounds
            neighbor = state[:]
            new_index = nx * 3 + ny
            neighbor[empty_tile_index], neighbor[new_index] = neighbor[new_index], neighbor[empty_tile_index]
            neighbors.append(neighbor)
    
    return neighbors

# A* algorithm
def a_star(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    
    came_from = {tuple(start): None}
    cost_so_far = {tuple(start): 0}
    
    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in get_neighbors(current):
            new_cost = cost_so_far[tuple(current)] + 1  # Cost of 1 for each move
            
            if tuple(neighbor) not in cost_so_far or new_cost < cost_so_far[tuple(neighbor)]:
                cost_so_far[tuple(neighbor)] = new_cost
                priority = new_cost + misplaced_tiles(neighbor, goal)
                heapq.heappush(priority_queue, (priority, neighbor))
                came_from[tuple(neighbor)] = current
    
    return None

# Function to reconstruct the path from start to goal
def reconstruct_path(came_from, current):
    path = []
    while current is not None:
        path.append(current)
        current = came_from[tuple(current)]
    return path[::-1]

# Helper function to flatten a 2D matrix to 1D list
def flatten(matrix):
    return [item for sublist in matrix for item in sublist]

# Main function to take matrix-style user input and solve the puzzle
if __name__ == "__main__":
    print("Enter the 8-puzzle initial state (as a 3x3 grid, row by row):")
    start_matrix = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(3)]
    start_state = flatten(start_matrix)
    
    print("Enter the goal state (as a 3x3 grid, row by row):")
    goal_matrix = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(3)]
    goal_state = flatten(goal_matrix)
    
    path = a_star(start_state, goal_state)
    
    if path:
        print(f"Solved in {len(path) - 1} moves:")
        for step in path:
            print(step[:3])
            print(step[3:6])
            print(step[6:])
            print()
    else:
        print("No solution found.")
