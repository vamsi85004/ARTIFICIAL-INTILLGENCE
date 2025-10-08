# Python Program to simulate the Vacuum Cleaner Problem

def vacuum_cleaner():
    # Take user input for room conditions
    goal_state = {'A': '0', 'B': '0'}  # 0 means Clean
    print("Enter the status of rooms: 1 for Dirty, 0 for Clean")
    room_A = input("Room A: ")
    room_B = input("Room B: ")
    current_state = {'A': room_A, 'B': room_B}

    # Take the current position of the vacuum cleaner
    position = input("Enter current position (A or B): ").upper()

    # Display the initial state
    print("\nInitial State:", current_state, "Vacuum at:", position)

    # Cleaning process
    cost = 0

    # If the current room is dirty, clean it
    if current_state[position] == '1':
        print(f"Room {position} is Dirty. Cleaning now...")
        current_state[position] = '0'
        cost += 1
        print(f"Room {position} is now Clean.")

    # Move to the other room
    if position == 'A':
        position = 'B'
    else:
        position = 'A'
    cost += 1
    print(f"Moved to Room {position}.")

    # Clean the new room if it’s dirty
    if current_state[position] == '1':
        print(f"Room {position} is Dirty. Cleaning now...")
        current_state[position] = '0'
        cost += 1
        print(f"Room {position} is now Clean.")
    else:
        print(f"Room {position} is already Clean.")

    # Display final state and performance cost
    print("\nFinal State:", current_state)
    print("Performance Measure (Total Actions):", cost)
    print("Goal State:", goal_state)

# Run the program
vacuum_cleaner()
