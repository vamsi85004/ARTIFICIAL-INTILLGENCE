


A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


rows = len(A)
cols = len(A[0])
transpose = [[0 for _ in range(rows)] for _ in range(cols)]


for i in range(rows):
    for j in range(cols):
        transpose[j][i] = A[i][j]


print("Original Matrix:")
for row in A:
    print(row)

print("\nTranspose of the Matrix:")
for row in transpose:
    print(row)
