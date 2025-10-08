# Missionaries and Cannibals Problem using BFS

from collections import deque

# State representation: (missionaries_left, cannibals_left, boat_side)
# boat_side = 1 means boat on left, 0 means boat on right

def is_valid_state(m_left, c_left, m_right, c_right):
    # Check if numbers are valid and missionaries are not outnumbered
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False
    return True

def missionaries_and_cannibals():
    start_state = (3, 3, 1)  # 3 missionaries, 3 cannibals, boat on left
    goal_state = (0, 0, 0)   # everyone moved to right
    
    # Queue for BFS
    queue = deque()
    queue.append((start_state, []))  # state + path
    
    visited = set()
    
    while queue:
        (m_left, c_left, boat), path = queue.popleft()
        
        if (m_left, c_left, boat) in visited:
            continue
        visited.add((m_left, c_left, boat))
        
        # Goal check
        if (m_left, c_left, boat) == goal_state:
            print("\nSolution Path (each step shows: missionaries_left, cannibals_left, boat_side):\n")
            for step in path + [goal_state]:
                print(step)
            return
        
        # Generate possible moves
        if boat == 1:  # boat on left side → move to right
            direction = -1
            new_boat = 0
        else:  # boat on right side → move to left
            direction = 1
            new_boat = 1
        
        # Possible moves: (M, C)
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        
        for m, c in moves:
            new_m_left = m_left + direction * m
            new_c_left = c_left + direction * c
            new_m_right = 3 - new_m_left
            new_c_right = 3 - new_c_left
            
            if is_valid_state(new_m_left, new_c_left, new_m_right, new_c_right):
                new_state = (new_m_left, new_c_left, new_boat)
                queue.append((new_state, path + [ (m_left, c_left, boat) ]))
    
    print("No solution found.")

# Run the solver
missionaries_and_cannibals()
S
