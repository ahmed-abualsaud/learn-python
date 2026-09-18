import numpy as np

# Create a 6×6 matrix containing numbers from 0 to 35
a = np.arange(36).reshape(6, 6)

print("Original matrix:\n", a)

#========================================================================================================
print('\n')

# Access the element at row 3, column 1
# (Remember: indexing starts from 0)
c = a[3, 1]

print("a[3, 1] (element at row 3, column 1):")
print(c)

#========================================================================================================
print('\n')

# Select all columns from row 3
# ':' means "take everything" along that axis
d = a[3, :]

print("a[3, :] (entire row at index 3):")
print(d)

#========================================================================================================
print('\n')

# Select all rows from column 2
e = a[:, 2]

print("a[:, 2] (entire column at index 2):")
print(e)

#========================================================================================================
print('\n')

# Select columns 1 and 2 from every row
# The stop index (3) is excluded
f = a[:, 1:3]

print("a[:, 1:3] (columns 1 and 2 from every row):")
print(f)

#========================================================================================================
print('\n')

# Select only row 1 while preserving the 2D shape
# 1:2 returns a slice (one-row matrix), not a 1D array
g = a[1:2, :]

print("a[1:2, :] (row 1 as a 2D matrix):")
print(g)


#========================================================================================================
print('\n')

# Select every second row and every third column
# Rows:    0, 2, 4
# Columns: 0, 3
c = a[::2, ::3]

print("a[::2, ::3] (every 2nd row and every 3rd column):")
print(c)

#========================================================================================================
print('\n')

# Reverse both rows and columns
# This produces the matrix flipped vertically and horizontally.
d = a[::-1, ::-1]

print("a[::-1, ::-1] (matrix reversed in both directions):")
print(d)

#========================================================================================================
print('\n')

# Reverse rows starting from the last row down to row 3 (exclusive of row 2)
# Reverse columns starting from the last column down to column 4
#
# Rows selected:    5, 4, 3
# Columns selected: 5, 4
e = a[:2:-1, :3:-1]

print("a[:2:-1, :3:-1] (reverse-selected rows and columns):")
print(e)

#========================================================================================================
print('\n')

# Start from row 2 and take every second row
# Start from column 3 and take every third column
#
# Rows:    2, 4
# Columns: 3
f = a[2::2, 3::3]

print("a[2::2, 3::3] (every 2nd row from row 2 and every 3rd column from column 3):")
print(f)

#========================================================================================================
print('\n')

# Select the last row and the last column
# This returns a 1×1 matrix containing the bottom-right element.
g = a[-1::, -1::]

print("a[-1::, -1::] (bottom-right element as a 2D matrix):")
print(g)