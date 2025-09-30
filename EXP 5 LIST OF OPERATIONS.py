# Python program to implement List operations

# 1. Nested List
nested_list = [[1, 2, 3], [4, 5, 6]]
print("Nested List:", nested_list)
print("Accessing element 5 from nested list:", nested_list[1][1])  # 5

# 2. Length of List
my_list = [10, 20, 30, 40, 50]
print("\nList:", my_list)
print("Length of the list:", len(my_list))

# 3. Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concat_list = list1 + list2
print("\nConcatenation of lists:", concat_list)

# 4. Membership
print("\nIs 20 in my_list?", 20 in my_list)
print("Is 100 not in my_list?", 100 not in my_list)

# 5. Iteration
print("\nIterating through my_list:")
for item in my_list:
    print(item, end=" ")

# 6. Indexing
print("\n\nIndexing examples:")
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# 7. Slicing
print("\nSlicing examples:")
print("First three elements:", my_list[0:3])
print("Elements from index 2 to end:", my_list[2:])
print("Every second element:", my_list[::2])
