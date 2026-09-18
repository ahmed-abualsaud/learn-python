import numpy as np

# Create two random 3×3 matrices.
# random.randint(low, high, size) generates random integers
# from 'low' (inclusive) to 'high' (exclusive).
a = np.random.randint(1, 4, size=9).reshape(3, 3)
b = np.random.randint(1, 4, size=9).reshape(3, 3)

print("Matrix a:")
print(a)

print("\nMatrix b:")
print(b)

#========================================================================================================
print('\n')

# Matrix multiplication (Dot Product)
#
# np.dot() performs TRUE matrix multiplication,
# NOT element-wise multiplication.
#
# Each element in the result is computed by:
#   - Taking one row from the first matrix.
#   - Taking one column from the second matrix.
#   - Multiplying corresponding elements.
#   - Summing the products.
#
# Formula:
# c[i, j] = Σ (a[i, k] * b[k, j])
#
# The number of columns in the first matrix must equal
# the number of rows in the second matrix.
c = np.dot(a, b)

print("Matrix multiplication using np.dot(a, b):")
print(c)

#========================================================================================================
print('\n')

# Create a 3×3 matrix filled with random integers
# from 5 (inclusive) to 20 (exclusive).
a = np.random.randint(5, 20, size=9).reshape(3, 3)

print("Original matrix:")
print(a)

#========================================================================================================
print('\n')

# Compute the sum of ALL elements in the matrix.
#
# np.sum() is a NumPy function that accepts an array
# as its argument.
b = np.sum(a)

print("Sum of all elements using np.sum(a):")
print(b)

#========================================================================================================
print('\n')

# Compute the sum of ALL elements in the matrix.
#
# This is the array method version of np.sum().
# It produces the same result as np.sum(a).
c = a.sum()

print("Sum of all elements using a.sum():")
print(c)

#========================================================================================================
print('\n')

# Compute the sum of each ROW.
#
# axis = 1 means:
#     Perform the operation across the columns,
#     producing one result for each row.
#
# Result:
# [sum(row0), sum(row1), sum(row2)]
d = a.sum(axis=1)

print("Sum of each row (axis = 1):")
print(d)

#========================================================================================================
print('\n')

# Compute the sum of each COLUMN.
#
# axis = 0 means:
#     Perform the operation down the rows,
#     producing one result for each column.
#
# Result:
# [sum(col0), sum(col1), sum(col2)]
e = a.sum(axis=0)

print("Sum of each column (axis = 0):")
print(e)

#========================================================================================================
print('\n')

# Create a 3×3 matrix filled with random integers
# from 5 (inclusive) to 20 (exclusive).
a = np.random.randint(5, 20, size=9).reshape(3, 3)

print("Original matrix:")
print(a)

#========================================================================================================
print('\n')

# Compute the arithmetic mean (average) of all elements.
#
# The mean represents the "center" of the data.
#
# Formula:
# Mean = (Sum of all values) / (Number of values)
#
# Example:
# Data = [2, 4, 6, 8]
#
# Mean = (2 + 4 + 6 + 8) / 4 = 5
#
# The mean is commonly used as a measure of the
# central tendency of a dataset.
b = a.mean()

print("Mean (average) of all elements:")
print(b)

#========================================================================================================
print('\n')

# Compute the standard deviation of all elements.
#
# Standard deviation measures how spread out the data
# is around the mean.
#
# Interpretation:
# - Small standard deviation:
#     Values are close to the mean.
#
# - Large standard deviation:
#     Values are spread far from the mean.
#
# The standard deviation is simply the square root
# of the variance.
#
# Formula:
# Standard Deviation = √Variance
#
# NumPy computes the population standard deviation
# by default (ddof=0).
c = a.std()

print("Standard deviation of all elements:")
print(c)

#========================================================================================================
print('\n')

# Compute the variance of all elements.
#
# Variance measures how much the data varies from
# the mean.
#
# Steps:
# 1. Compute the mean.
# 2. Subtract the mean from every value.
# 3. Square each difference.
# 4. Compute the average of those squared differences.
#
# Interpretation:
# - Small variance:
#     Data values are close together.
#
# - Large variance:
#     Data values are more spread out.
#
# The variance is always greater than or equal to zero.
#
# NumPy computes the population variance
# by default (ddof=0).
d = a.var()

print("Variance of all elements:")
print(d)