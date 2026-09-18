import numpy as np

# Create a 3×3 matrix filled with random integers
# from 5 (inclusive) to 20 (exclusive).
a = np.random.randint(5, 20, size=9).reshape(3, 3)

print("Original matrix:")
print(a)

#========================================================================================================
print('\n')

# Compute the correlation coefficient matrix.
#
# Correlation measures the STRENGTH and DIRECTION
# of the linear relationship between variables.
#
# Unlike covariance, correlation is NORMALIZED,
# so its values are always between -1 and +1.
#
# Correlation coefficient (r):
#
#   r = +1
#       Perfect positive linear relationship.
#
#   r = 0
#       No linear relationship.
#
#   r = -1
#       Perfect negative linear relationship.
#
# By default, np.corrcoef() treats each ROW
# as a separate variable and each COLUMN
# as an observation.
#
# The result is a correlation matrix.
b = np.corrcoef(a)

print("Correlation coefficient matrix:")
print(b)

#========================================================================================================
print('\n')

# Create a random 3×3 matrix.
# random.randint(low, high, size) generates random integers
# from 'low' (inclusive) to 'high' (exclusive).
a = np.random.randint(5, 20, size=9).reshape(3, 3)

print("Original matrix:")
print(a)

#========================================================================================================
print('\n')

# Sort each COLUMN independently.
#
# axis = 0 means:
#     Move DOWN each column and sort its values.
#
# The values within each column are rearranged
# from smallest to largest.
#
# The rows themselves are NOT preserved.
#
# Result:
# Each column becomes sorted independently.
b = np.sort(a, axis=0)

print("Matrix sorted by columns (axis = 0):")
print(b)

#========================================================================================================
print('\n')

# Sort each ROW independently.
#
# axis = 1 means:
#     Move ACROSS each row and sort its values.
#
# The values within each row are rearranged
# from smallest to largest.
#
# The columns themselves are NOT preserved.
#
# Result:
# Each row becomes sorted independently.
c = np.sort(a, axis=1)

print("Matrix sorted by rows (axis = 1):")
print(c)

#========================================================================================================
print('\n')

# Create a random 3×3 matrix.
# random.randint(low, high, size) generates random integers
# from 'low' (inclusive) to 'high' (exclusive).
#
# IMPORTANT:
# Not every matrix has an inverse.
# If the determinant of the matrix is zero,
# np.linalg.inv() will raise a LinAlgError.
a = np.random.randint(1, 4, size=9).reshape(3, 3)

print("Original matrix (a):")
print(a)

#========================================================================================================
print('\n')

# Compute the inverse of matrix 'a'.
#
# The inverse of a matrix is analogous to the reciprocal
# of a number.
#
# For example:
#
# Number:
# 5 × (1/5) = 1
#
# Matrix:
# A × A⁻¹ = I
#
# where I is the identity matrix.
b = np.linalg.inv(a)

print("Inverse of matrix a:")
print(b)

#========================================================================================================
print('\n')

# Verify the inverse.
#
# Multiplying a matrix by its inverse should produce
# the identity matrix.
#
# Because floating-point arithmetic is not exact,
# very small numbers such as:
#
# 2.22044605e-16
#
# should be considered equal to zero.
c = np.dot(a, b)

print("a × inv(a):")
print(c)