# Python Program to solve the Water Jug Problem using BFS

from collections import deque

def water_jug_solver(jug1, jug2, target):
    # To keep track of visited states
    visited = set()
    
    # Queue for BFS: each state is represented as (x, y)
    # x = water in jug1, y = water in jug2
    queue = deque()
    queue.append((0, 0))  # Initially both jugs are empty
    
    while queue:
        x, y = queue.popleft()

        # If target is reached
        if x == target or y == target:
            print(f"Solution found: ({x}, {y})")
            return True

        # If the state is already visited, skip it
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Possible next states
        next_states = [
            (jug1, y),             # Fill jug1
            (x, jug2),             # Fill jug2
            (0, y),                # Empty jug1
            (x, 0),                # Empty jug2
            # Pour jug1 -> jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),
            # Pour jug2 -> jug1
            (x + min(y, jug1 - x), y - min(y, jug1 - x))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)
                print(f"Visited: {state}")

    print("No solution possible.")
    return False


# Example Input
jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

# Solve
water_jug_solver(jug1, jug2, target)
