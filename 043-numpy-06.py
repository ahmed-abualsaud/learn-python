import numpy as np

# creates 2*2 matrix, note the ; in the string, it means new row in the mtrix
a = np.matrix('{} {} ; {} {}'.format(1, 2, 3, 4)) 
print('matrix a:\n', a)

# create 2*3 matrix
b = np.matrix('{} {} {} ; {} {} {}'.format(1, 2, 3, 4, 5, 6))
print('matrix b:\n', b)


#========================================================================================================
print('\n')


a = np.arange(9).reshape(3, 3)
# trace() returns the sum of the main diagonal elements of a matrix.
# The main diagonal starts from the top-left corner to the bottom-right corner.
#
# Example:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
#
# Trace = 1 + 5 + 9 = 15
t = np.trace(a)

print('matrix 3*3:\n', a)
print('sum of the diagonal of the mtrix 3*3 is:', t)

a = np.arange(6).reshape(2, 3)
t = np.trace(a)

print('matrix 2*3:\n', a)
print('sum of the diagonal of the mtrix 2*3 is:', t)


#========================================================================================================
print('\n')


a = np.arange(9).reshape(3, 3)
# det() computes the determinant of a square matrix.
# The determinant is a single number that describes some important
# properties of a matrix:
#
# - det = 0  -> the matrix is singular (not invertible).
# - det != 0 -> the matrix has an inverse.
# - |det|    -> the scaling factor of area (2D) or volume (3D)
#               after the linear transformation.
# - The sign (+/-) indicates whether the transformation
#   preserves or reverses orientation.
det = np.linalg.det(a)

# eig() computes the eigenvalues and eigenvectors of a square matrix.
#
# Eigenvalue:
# A scalar (λ) that tells how much an eigenvector is stretched or compressed
# after applying the matrix transformation.
#
# Eigenvector:
# A non-zero vector whose direction does not change after the
# transformation (it may only be scaled or flipped).
#
# They satisfy the equation:
#
#     A * v = λ * v
#
# where:
#   A = matrix
#   v = eigenvector
#   λ = eigenvalue
#
# eig() returns:
#   - eigenvalues  : scaling factors (λ)
#   - eigenvectors : corresponding directions (v)
eig = np.linalg.eig(a)

print('matrix 3*3:\n', a)
print ('the determinant of matrix 3*3:', det)
print('eigen values of matrix 3*3:', eig.eigenvalues)
print('eigen vectors of matrix 3*3:\n', eig.eigenvectors)


#========================================================================================================
print('\n')


a = np.arange(10)  # Create a 1D array containing numbers from 0 to 9

print('matrix a:', a)

# Access individual elements by their index (indexing starts from 0)
print('first two items of matrix a:', a[0], a[1])

# Slice the array from index 0 up to (but not including) index 3
print('first three items of matrix a:', a[0:3])

# Slice with a step of 2:
# start at index 0, stop before index 5, take every second element
# Result: [0, 2, 4]
print('first three even items of matrix a:', a[0:5:2])

#========================================================================================================
print('\n')

# Create a 3×3 matrix containing numbers from 0 to 8
b = np.arange(9).reshape(3, 3)

print('matrix b:\n', b)

# Access the first row of the matrix
print('first row of matrix b:', b[0])

# Slice the first row:
# rows:    0
# columns: 0 to 1 (stop before column 2)
# Result: [0, 1]
print('first two elements of the first row of matrix b:', b[0, 0:2])


#========================================================================================================
print('\n')


# Create a 6×6 matrix containing numbers from 0 to 35
a = np.arange(36).reshape(6, 6)

print("Original matrix:\n", a)

# Access the row at index 3 (the fourth row)
c = a[3]

print("a[3] (row at index 3):")
print(c)

#========================================================================================================
print('\n')

# Slice rows from index 3 to the end.
# The stop index (9) is larger than the number of rows,
# so NumPy simply stops at the last row.
d = a[3:9]

print("a[3:9] (rows from index 3 to the end):")
print(d)

#========================================================================================================
print('\n')

# Slice rows starting from index 3, taking every second row.
# Again, index 9 is beyond the matrix, so slicing stops at the end.
e = a[3:9:2]

print("a[3:9:2] (every second row from index 3):")
print(e)

#========================================================================================================
print('\n')

# Access the last row using negative indexing
f = a[-1]

print("a[-1] (last row):")
print(f)

#========================================================================================================
print('\n')

# Access the third row from the end
g = a[-3]

print("a[-3] (third row from the end):")
print(g)
