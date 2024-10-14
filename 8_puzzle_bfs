from collections import deque


class Node:
    def __init__(self, puzzle, x, y, parent=None):
        self.puzzle = [row[:] for row in puzzle]
        self.x = x
        self.y = y
        self.parent = parent


goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def is_goal(puzzle):
    return puzzle == goal


def print_puzzle(puzzle):
    for row in puzzle:
        print(' '.join(str(x) if x != 0 else ' ' for x in row))
    print()


def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3


def bfs(root):
    queue = deque([root])
    visited = set()
   
    while queue:
        node = queue.popleft()
       
        if is_goal(node.puzzle):
            print("Solution found:")
            path = []
            while node:
                path.append(node.puzzle)
                node = node.parent
            for state in reversed(path):
                print_puzzle(state)
            return True
       
        puzzle_tuple = tuple(map(tuple, node.puzzle))
        if puzzle_tuple in visited:
            continue
        visited.add(puzzle_tuple)
       
        for i in range(4):
            new_x = node.x + dx[i]
            new_y = node.y + dy[i]
           
            if is_valid(new_x, new_y):
                new_puzzle = [row[:] for row in node.puzzle]
                new_puzzle[node.x][node.y], new_puzzle[new_x][new_y] = new_puzzle[new_x][new_y], new_puzzle[node.x][node.y]
               
                new_puzzle_tuple = tuple(map(tuple, new_puzzle))
                if new_puzzle_tuple not in visited:
                    new_node = Node(new_puzzle, new_x, new_y, node)
                    queue.append(new_node)
   
    print("No solution found.")
    return False


def main():
    initial_puzzle = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]
   
    print("Initial Puzzle:")
    print_puzzle(initial_puzzle)
   
    x, y = [(i, j) for i in range(3) for j in range(3) if initial_puzzle[i][j] == 0][0]
   
    root = Node(initial_puzzle, x, y)
   
    if not bfs(root):
        print("Failed to find a solution.")


if __name__ == "__main__":
    main()
