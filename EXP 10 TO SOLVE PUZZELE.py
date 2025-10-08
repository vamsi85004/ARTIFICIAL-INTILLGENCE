# 8-Puzzle Problem using A* Search Algorithm

import heapq

# Define the goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents the blank space

# Function to calculate Manhattan Distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance

# Function to find the position of the blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Function to generate possible moves
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Convert state (list of lists) to a tuple for hashing
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

# A* Search Algorithm
def solve_puzzle(start_state):
    pq = []
    heapq.heappush(pq, (manhattan_distance(start_state), 0, start_state, []))
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == goal_state:
            return path + [current]

        visited.add(state_to_tuple(current))

        for neighbor in get_neighbors(current):
            if state_to_tuple(neighbor) not in visited:
                heapq.heappush(pq, (g + 1 + manhattan_distance(neighbor), g + 1, neighbor, path + [current]))
    return None

# Input: initial state
start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

# Solve the puzzle
solution = solve_puzzle(start_state)

# Display the result
if solution:
    print("Steps to reach the goal:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
