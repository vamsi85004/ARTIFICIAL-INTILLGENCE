# Python Program to solve the Cryptarithmetic Problem: SEND + MORE = MONEY

import itertools

def solve_cryptarithmetic():
    # Unique letters in the puzzle
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    
    # Digits from 0 to 9
    digits = range(10)
    
    # Try all possible digit assignments using permutations
    for perm in itertools.permutations(digits, len(letters)):
        assign = dict(zip(letters, perm))
        
        # Ensure no leading zeros for SEND or MORE or MONEY
        if assign['S'] == 0 or assign['M'] == 0:
            continue
        
        # Convert words to numbers using the mapping
        send = assign['S']*1000 + assign['E']*100 + assign['N']*10 + assign['D']
        more = assign['M']*1000 + assign['O']*100 + assign['R']*10 + assign['E']
        money = assign['M']*10000 + assign['O']*1000 + assign['N']*100 + assign['E']*10 + assign['Y']
        
        # Check if the equation holds
        if send + more == money:
            print("Solution Found!")
            print(f"SEND = {send}")
            print(f"MORE = {more}")
            print(f"MONEY = {money}")
            print("Letter Mapping:", assign)
            return  # stop after finding first solution

    print("No solution found.")

# Run the solver
solve_cryptarithmetic()
