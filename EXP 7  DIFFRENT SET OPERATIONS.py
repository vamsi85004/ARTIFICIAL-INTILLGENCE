# Python program to illustrate different set operations

# Define two sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

print("Set A:", setA)
print("Set B:", setB)

# 1. Union - combines all elements from both sets
union_set = setA.union(setB)
print("\nUnion of A and B:", union_set)

# 2. Intersection - elements common to both sets
intersection_set = setA.intersection(setB)
print("Intersection of A and B:", intersection_set)

# 3. Difference - elements in A but not in B
difference_set = setA.difference(setB)
print("Difference of A and B (A - B):", difference_set)

# 4. Symmetric Difference - elements in A or B but not both
sym_diff_set = setA.symmetric_difference(setB)
print("Symmetric Difference of A and B:", sym_diff_set)

# 5. Membership Test
print("\nIs 3 in Set A?", 3 in setA)
print("Is 6 not in Set A?", 6 not in setA)

# 6. Adding an element
setA.add(10)
print("\nAfter adding 10 to Set A:", setA)

# 7. Removing an element
setA.remove(2)
print("After removing 2 from Set A:", setA)

# 8. Iteration through a set
print("\nIterating through Set B:")
for elem in setB:
    print(elem, end=" ")
