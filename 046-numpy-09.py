import numpy as np

# Create a 4×4 matrix containing numbers from 0 to 15
a = np.arange(16).reshape(4, 4)

print("Original matrix:\n", a)

#========================================================================================================
print('\n')

# Chained indexing:
#
# Step 1: a[2]
#         Selects the third row of the matrix.
#
# Step 2: [1]
#         Selects the second element from that row.
#
# This is equivalent to:
#     a[2, 1]
#
# The result is a single scalar value.
b = a[2][1]

print("a[2][1] (element at row 2, column 1):")
print(b)

#========================================================================================================
print('\n')

# Create a 1D array
x = np.array([11, 22, 33, 44, 55, 66, 77, 88])

print("Original array:")
print(x)

#========================================================================================================
print('\n')

# split() divides an array at the specified indices.
# The tuple (3, 6) means:
#   - First split before index 3
#   - Second split before index 6
#
# Result:
# x[:3], x[3:6], x[6:]
x1, x2, x3 = np.split(x, (3, 6))

print("Split at indices (3, 6):")
print("First part :", x1)
print("Second part:", x2)
print("Third part :", x3)

#========================================================================================================
print('\n')

# Split before index 1 and before index 5
#
# Result:
# x[:1], x[1:5], x[5:]
x1, x2, x3 = np.split(x, (1, 5))

print("Split at indices (1, 5):")
print("First part :", x1)
print("Second part:", x2)
print("Third part :", x3)

#========================================================================================================
print('\n')

# The split indices do NOT have to be sorted.
# NumPy processes them in the given order.
#
# Result:
# x[:6], x[6:3], x[3:]
#
# Notice that x[6:3] is an empty array because
# the start index is greater than the stop index.
x1, x2, x3 = np.split(x, (6, 3))

print("Split at indices (6, 3):")
print("First part :", x1)
print("Second part:", x2)
print("Third part :", x3)

#========================================================================================================
print('\n')

# Split before index 0 and before index 3.
#
# x[:0] is empty because nothing comes before index 0.
x1, x2, x3 = np.split(x, (0, 3))

print("Split at indices (0, 3):")
print("First part :", x1)
print("Second part:", x2)
print("Third part :", x3)

#========================================================================================================
print('\n')

# Split before index 4 and before index 0.
#
# x[4:0] is empty because the start index is greater than the stop index.
x1, x2, x3 = np.split(x, (4, 0))

print("Split at indices (4, 0):")
print("First part :", x1)
print("Second part:", x2)
print("Third part :", x3)

#========================================================================================================
print('\n')

# Create two 2×2 matrices
a = np.arange(4).reshape(2, 2)
b = 2 * np.arange(4).reshape(2, 2)

print("Matrix a:")
print(a)

print("\nMatrix b:")
print(b)

#========================================================================================================
print('\n')

# vstack() (Vertical Stack)
# Stacks arrays vertically by adding the rows of one matrix
# below the rows of another matrix.
#
# The number of columns must be the same.
#
# Shape:
# a : (2, 2)
# b : (2, 2)
# Result : (4, 2)
c = np.vstack((a, b))

print("Vertical stack using np.vstack((a, b)):")
print(c)

#========================================================================================================
print('\n')

# Create the matrices again
a = np.arange(4).reshape(2, 2)
b = 2 * np.arange(4).reshape(2, 2)

print("Matrix a:")
print(a)

print("\nMatrix b:")
print(b)

#========================================================================================================
print('\n')

# hstack() (Horizontal Stack)
# Stacks arrays horizontally by placing one matrix
# to the right of another matrix.
#
# The number of rows must be the same.
#
# Shape:
# a : (2, 2)
# b : (2, 2)
# Result : (2, 4)
c = np.hstack((a, b))

print("Horizontal stack using np.hstack((a, b)):")
print(c)

#========================================================================================================
print('\n')

# Create two random 3×3 matrices.
# random.randint(low, high, size) generates random integers
# from 'low' (inclusive) to 'high' (exclusive).
a = np.random.randint(5, 20, size=9).reshape(3, 3)
b = np.random.randint(5, 20, size=9).reshape(3, 3)

print("Matrix a:")
print(a)

print("\nMatrix b:")
print(b)

#========================================================================================================
print('\n')

# concatenate() joins multiple arrays along the specified axis.
#
# axis = 0
# --------
# Join the matrices vertically by adding more rows.
#
# Shape:
# a : (3, 3)
# b : (3, 3)
# Result : (6, 3)
#
# Both matrices must have the same number of columns.
c = np.concatenate([a, b], axis=0)

print("Concatenate along axis = 0 (add rows):")
print(c)

#========================================================================================================
print('\n')

# Create two new random matrices
a = np.random.randint(5, 20, size=9).reshape(3, 3)
b = np.random.randint(5, 20, size=9).reshape(3, 3)

print("Matrix a:")
print(a)

print("\nMatrix b:")
print(b)

#========================================================================================================
print('\n')

# concatenate() along axis = 1
#
# Join the matrices horizontally by adding more columns.
#
# Shape:
# a : (3, 3)
# b : (3, 3)
# Result : (3, 6)
#
# Both matrices must have the same number of rows.
c = np.concatenate([a, b], axis=1)

print("Concatenate along axis = 1 (add columns):")
print(c)