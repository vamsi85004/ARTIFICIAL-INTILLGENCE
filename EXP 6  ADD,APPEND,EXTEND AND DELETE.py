# Python program to demonstrate list methods

# Initial list
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# 1. Add (Insert) - insert element at a specific position
my_list.insert(2, 25)  # Insert 25 at index 2
print("\nAfter insert(2, 25):", my_list)

# 2. Append - add element at the end
my_list.append(60)
print("After append(60):", my_list)

# 3. Extend - add multiple elements at the end
my_list.extend([70, 80, 90])
print("After extend([70, 80, 90]):", my_list)

# 4. Delete
# a) Using remove() to delete by value
my_list.remove(25)  # Removes first occurrence of 25
print("After remove(25):", my_list)

# b) Using pop() to delete by index
deleted_item = my_list.pop(3)  # Deletes element at index 3
print(f"After pop(3) (deleted {deleted_item}):", my_list)

# c) Using del to delete a slice
del my_list[2:4]  # Deletes elements from index 2 to 3
print("After del my_list[2:4]:", my_list)
