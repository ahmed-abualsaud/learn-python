import numpy as np

l = [1, 2, 3, 4]
m = np.array(l)  # Create a 1×4 matrix (1D NumPy array)

print('matrix {}:'.format(l), m)


#========================================================================================================
print('\n')


l = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
m = np.array(l)  # Create a 2×4 matrix (2D NumPy array)

print('matrix {}:\n'.format(l), m)


#========================================================================================================
print('\n')


l = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]
m = np.array(l)  # Create a 3×4 matrix (2D NumPy array)

print('matrix {}:\n'.format(l), m)


#========================================================================================================
print('\n')


l = [
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 0, 1, 2]
    ],
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 0, 1, 2]
    ]
]
t = np.array(l)  # Create a 3D tensor with shape (2, 3, 4)

print('tensor {}:\n'.format(l), t)


#========================================================================================================
print('\n')


a = np.array([range(i, i + 3) for i in [2, 4, 6]])

print(a)


#========================================================================================================
print('\n')


# Structured NumPy array:
# Each element is a record (similar to a row in a database table)
# containing fields with different data types.
#
# Field definitions:
#   name   -> Unicode string (up to 5 characters)
#   number -> 16-bit integer (int16)
#   value  -> 32-bit floating-point number (float32)

a = np.array(
    [('x', 3, 4.2),
     ('y', 4, 5.3),
     ('z', 5, 6.3)],
    dtype=[
        ('name', 'U5'),
        ('number', 'i2'),
        ('value', 'f4')
    ]
)

print(a)

# Access fields by their names
print(a['name'])     # ['x' 'y' 'z']
print(a['number'])   # [3 4 5]
print(a['value'])    # [4.2 5.3 6.3]


#========================================================================================================
print('\n')


e = np.empty((3,2)) # create an empty 3*2 matrix

print('empty matrix is:\n', e)