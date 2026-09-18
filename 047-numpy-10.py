import numpy as np

# Create a 3×3 matrix filled with random integers
# from 5 (inclusive) to 20 (exclusive).
a = np.random.randint(5, 20, size=9).reshape(3, 3)

print("Original matrix:")
print(a)

#========================================================================================================
print('\n')

# max() returns the largest value in the entire matrix.
b = np.max(a)

print("Maximum value in the matrix:")
print(b)

#========================================================================================================
print('\n')

# min() returns the smallest value in the entire matrix.
c = np.min(a)

print("Minimum value in the matrix:")
print(c)

#========================================================================================================
print('\n')

# argmax() returns the index of the largest element.
#
# For multi-dimensional arrays, NumPy first flattens the array
# into a 1D array using row-major (C-style) order, then returns
# the index of the maximum element in that flattened array.
d = np.argmax(a)

print("Index of the maximum element (flattened index):")
print(d)

#========================================================================================================
print('\n')

# argmin() returns the index of the smallest element.
#
# Like argmax(), the index is relative to the flattened array.
e = np.argmin(a)

print("Index of the minimum element (flattened index):")
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

# VARIANCE
# --------
# Variance measures how spread out the data is around its mean.
#
# It is the average of the squared distances from the mean.
#
# Steps:
#   1. Compute the mean of the data.
#   2. Subtract the mean from every value.
#   3. Square each difference (so negatives become positive).
#   4. Compute the average of those squared differences.
#
# Interpretation:
#   - Small variance -> values are close to the mean.
#   - Large variance -> values are widely spread.
#   - Variance is always >= 0.
#   - Variance equals 0 only when all values are identical.
#
# Example:
# Data: [10, 11, 12]
# Mean = 11
#
# Deviations:
# [-1, 0, 1]
#
# Squared deviations:
# [1, 0, 1]
#
# Variance = (1 + 0 + 1) / 3 = 0.667
#
# Note:
# The unit of variance is squared.
# If the data is measured in meters,
# the variance is measured in square meters.
#
# NumPy uses population variance by default (ddof=0).
b = np.var(a)

print("Variance of all elements:")
print(b)

#========================================================================================================
print('\n')

# COVARIANCE
# ----------
# Covariance measures how TWO variables change together.
#
# Unlike variance (which measures the spread of ONE variable),
# covariance compares TWO variables.
#
# Interpretation:
#
# Positive covariance:
#     When one variable increases,
#     the other tends to increase.
#
# Negative covariance:
#     When one variable increases,
#     the other tends to decrease.
#
# Covariance near zero:
#     No clear linear relationship.
#
# Example:
#
# Height : [160, 170, 180]
# Weight : [55, 65, 75]
#
# Taller people tend to weigh more,
# so the covariance is positive.
#
# Another example:
#
# Speed : [20, 40, 60]
# Travel Time : [30, 15, 10]
#
# As speed increases,
# travel time decreases,
# so the covariance is negative.
#
# np.cov() returns a covariance matrix.
#
# For three variables:
#
#        Var1   Var2   Var3
# Var1     •      •      •
# Var2     •      •      •
# Var3     •      •      •
#
# The diagonal contains the variance of each variable.
#
# The off-diagonal values contain the covariance
# between pairs of variables.
#
# By default:
#   each ROW is treated as a variable,
#   each COLUMN is treated as an observation.
#
# If your columns represent variables (common in
# machine learning datasets), use:
#
# np.cov(a, rowvar=False)
#
# so each column is treated as one variable.
c = np.cov(a)

print("Covariance matrix:")
print(c)