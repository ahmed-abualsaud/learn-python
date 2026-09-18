import numpy as np

# Create a 4×4 matrix containing numbers from 0 to 15
a = np.arange(16).reshape(4, 4)

print("Original matrix:\n", a)

#========================================================================================================
print('\n')

# Modify a single element.
# Set the element at row 2, column 3 to 0.
a[2, 3] = 0

print("After setting a[2, 3] = 0:")
print(a)

#========================================================================================================
print('\n')

# Modify an entire column.
# ':' means "all rows", so every element in column 3 becomes 0.
a[:, 3] = 0

print("After setting the entire column 3 to 0 (a[:, 3] = 0):")
print(a)

#========================================================================================================
print('\n')

# Modify an entire row.
# ':' means "all columns", so every element in row 2 becomes 0.
a[2, :] = 0

print("After setting the entire row 2 to 0 (a[2, :] = 0):")
print(a)

#========================================================================================================
print('\n')

# Modify the entire matrix.
# ':, :' selects every row and every column.
# Every element in the matrix becomes 0.
a[:, :] = 0

print("After setting every element in the matrix to 0 (a[:, :] = 0):")
print(a)

#========================================================================================================
print('\n')

# Create a 4×4 matrix containing numbers from 0 to 15
a = np.arange(16).reshape(4, 4)

print("Original matrix:\n", a)

#========================================================================================================
print('\n')

# Create a slice containing columns 1 and 2 from every row.
# This does NOT create a copy.
# Instead, b is a VIEW of the original matrix.
# Any modification to 'a' will also be visible in 'b',
# because both share the same underlying data.
b = a[:, 1:3]

print("View of columns 1 and 2 (b = a[:, 1:3]):")
print(b)

#========================================================================================================
print('\n')

# Modify every element in the original matrix.
# Since 'b' is only a view, it will reflect these changes automatically.
a[:, :] = 5

print("Original matrix after setting all elements to 5:")
print(a)

#========================================================================================================
print('\n')

# Notice that 'b' has changed as well,
# even though we never modified 'b' directly.
# This happens because 'b' shares the same memory as 'a'.
print("View b after modifying a:")
print(b)

#========================================================================================================
print('\n')

# Create a 4×4 matrix containing numbers from 0 to 15
a = np.arange(16).reshape(4, 4)

print("Original matrix:\n", a)

#========================================================================================================
print('\n')

# Create a COPY of columns 1 and 2 from every row.
# Unlike slicing alone, copy() allocates new memory.
# Changes made to 'a' will NOT affect 'b',
# and changes made to 'b' will NOT affect 'a'.
b = a[:, 1:3].copy()

print("Copy of columns 1 and 2 (b = a[:, 1:3].copy()):")
print(b)

#========================================================================================================
print('\n')

# Modify every element in the original matrix.
# Since 'b' is an independent copy,
# these changes will NOT appear in 'b'.
a[:, :] = 5

print("Original matrix after setting all elements to 5:")
print(a)

#========================================================================================================
print('\n')

# Notice that 'b' still contains the original values.
# This is because b owns its own memory.
print("Copy b after modifying a:")
print(b)

#========================================================================================================
print('\n')

# Create a 3×3×2 tensor containing numbers from 0 to 17.
#
# Shape:
#   Axis 0 -> 3 layers
#   Axis 1 -> 3 rows in each layer
#   Axis 2 -> 2 columns in each row
a = np.arange(18).reshape(3, 3, 2)

print("Original 3D tensor:\n", a)

#========================================================================================================
print('\n')

# Select the layer at index 1.
# The result is a 2D matrix with shape (3, 2).
c = a[1]

print("a[1] (layer at index 1):")
print(c)

#========================================================================================================
print('\n')

# Select the row at index 2 from layer 1.
# The result is a 1D array with shape (2,).
d = a[1, 2]

print("a[1, 2] (row 2 from layer 1):")
print(d)

#========================================================================================================
print('\n')

# Select a single element.
#
# Index order:
#   a[layer, row, column]
#
# Layer  : 2
# Row    : 2
# Column : 1
e = a[2, 2, 1]

print("a[2, 2, 1] (element at layer 2, row 2, column 1):")
print(e)