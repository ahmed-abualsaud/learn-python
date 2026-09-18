import numpy as np

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

# Matrix addition
#
# The '+' operator performs ELEMENT-WISE addition.
# Each element in 'a' is added to the corresponding
# element in 'b'.
#
# c[i, j] = a[i, j] + b[i, j]
#
# Both matrices must have compatible shapes.
c = a + b

print("Element-wise addition (a + b):")
print(c)

#========================================================================================================
print('\n')

# Matrix subtraction
#
# The '-' operator performs ELEMENT-WISE subtraction.
#
# d[i, j] = a[i, j] - b[i, j]
d = a - b

print("Element-wise subtraction (a - b):")
print(d)

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

# Matrix multiplication using '*'
#
# IMPORTANT:
# The '*' operator DOES NOT perform matrix multiplication.
#
# It performs ELEMENT-WISE multiplication.
#
# c[i, j] = a[i, j] * b[i, j]
c = a * b

print("Element-wise multiplication (a * b):")
print(c)

#========================================================================================================
print('\n')

# Element-wise division
#
# Each element of 'a' is divided by the
# corresponding element of 'b'.
#
# d[i, j] = a[i, j] / b[i, j]
#
# The result is usually a floating-point array.
d = a / b

print("Element-wise division (a / b):")
print(d)

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

# Apply the sine function to every element of matrix 'a'.
#
# NumPy's trigonometric functions use RADIANS, not degrees.
#
# c[i, j] = sin(a[i, j])
c = np.sin(a)

print("Element-wise sine of matrix a (np.sin(a)):")
print(c)

#========================================================================================================
print('\n')

# Raise every element of matrix 'b' to the power of 2.
#
# d[i, j] = b[i, j]²
#
# This is equivalent to:
# np.power(b, 2)
d = b ** 2

print("Element-wise square of matrix b (b ** 2):")
print(d)

#========================================================================================================
print('\n')

# Compute the natural logarithm (base e) of every element in matrix 'a'.
#
# e[i, j] = ln(a[i, j])
#
# np.log() computes the natural logarithm (base e),
# NOT the common logarithm (base 10).
#
# Since all values in 'a' are between 5 and 19,
# the logarithm is well-defined.
e = np.log(a)

print("Element-wise natural logarithm of matrix a (np.log(a)):")
print(e)

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

# Scalar multiplication
#
# Every element in matrix 'a' is multiplied by the scalar value 3.
#
# c[i, j] = a[i, j] * 3
#
# The shape of the matrix does not change.
c = a * 3

print("Matrix a after multiplying every element by 3 (a * 3):")
print(c)

#========================================================================================================
print('\n')

# Scalar division
#
# Every element in matrix 'b' is divided by the scalar value 5.
#
# d[i, j] = b[i, j] / 5
#
# The result is typically a floating-point matrix because
# division in NumPy produces floating-point values.
d = b / 5

print("Matrix b after dividing every element by 5 (b / 5):")
print(d)