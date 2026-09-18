import numpy as np

# Path to the text file.
#
# In Windows, backslashes '\' must either be escaped ('\\')
# or the string should be written as a raw string:
#
# r'./data/numpy-data-1.txt'
fname = r'./data/numpy-data-1.txt'

#========================================================================================================
print('\n')

# Define the structure (data type) of each row that will
# be read from the file.
#
# This is called a STRUCTURED DATA TYPE.
#
# Each tuple has the form:
#
# (field_name, data_type)
#
# Field 1:
#   gender -> one-character string
#
# '|S1'
#   |  = byte order is not important
#   S  = byte string
#   1  = maximum length is 1 character
#
# Field 2:
#   height -> 64-bit floating-point number
#
# 'f8'
#   f = floating-point number
#   8 = 8 bytes (64 bits)
dtype1 = np.dtype([
    ('gender', '|S1'),
    ('height', 'f8')
])

#========================================================================================================
print('\n')

# Read data from the text file.
#
# np.loadtxt() loads numerical or structured data
# from a text file.
#
# Parameters:
#
# fname
#     Path of the file.
#
# dtype=dtype1
#     Read each row using the structured data type
#     defined above.
#
# skiprows=9
#     Ignore the first 9 lines of the file.
#     These lines often contain headers or comments.
#
# usecols=(1, 3)
#     Read only columns 1 and 3.
#
#     Column indexing starts from zero:
#
#     Column 0
#     Column 1  ← gender
#     Column 2
#     Column 3  ← height
a = np.loadtxt(
    fname,
    dtype=dtype1,
    skiprows=9,
    usecols=(1, 3)
)

#========================================================================================================
print('\n')

print("Structured array loaded from the file:")
print(a)

print("\nData type of the array:")
print(a.dtype)

print("\nFirst record:")
print(a[0])

print("\nGender column:")
print(a['gender'])

print("\nHeight column:")
print(a['height'])



#========================================================================================================
print('\n')

# Path to the text file.
#
# Using a raw string (r'...') prevents Python from
# interpreting '\' as an escape character.
fname = r'./data/numpy-data-2.txt'

#========================================================================================================
print('\n')

# Load numerical data from the text file.
#
# np.loadtxt() reads the file and converts it into
# a NumPy array.
#
# Parameters:
#
# skiprows=3
#     Ignore the first three lines of the file.
#     These lines usually contain titles or comments.
#
# unpack=True
#     Instead of returning one 2D array, transpose the
#     data and return one array for each column.
#
# Suppose the file contains:
#
# X   Y   Z
# ---------
# 1   2   3
# 4   5   6
# 7   8   9
#
# Without unpack=True:
#
# [[1. 2. 3.]
#  [4. 5. 6.]
#  [7. 8. 9.]]
#
# With unpack=True:
#
# a = [1. 4. 7.]
# b = [2. 5. 8.]
# c = [3. 6. 9.]
#
# now unpack=True converts each COLUMN to a ROW
# Each variable receives one ROW (a COLUMN in the file) from the file.
a, b, c = np.loadtxt(
    fname,
    skiprows=3,
    unpack=True
)

#========================================================================================================
print('\n')

print("First column:")
print(a)

print("\nSecond column:")
print(b)

print("\nThird column:")
print(c)

#========================================================================================================
print('\n')

# Path to the CSV file.
#
# Using a raw string (r'...') prevents Python from
# interpreting '\' as an escape character.
fname = r'./data/numpy-data-3.txt'

#========================================================================================================
print('\n')

# Load data from a text file using np.genfromtxt().
#
# Unlike np.loadtxt(), np.genfromtxt() can:
#
# • Handle missing values.
# • Read mixed data types.
# • Automatically fill missing entries.
# • Work with structured arrays.
#
# This makes it a better choice for real-world datasets.
data = np.genfromtxt(

    fname,

    # Skip the first line of the file.
    # This is usually the header containing
    # the column names.
    skip_header=1,

    # Define the data type of each column.
    #
    # student -> unsigned 64-bit integer
    # gender  -> one-byte string
    # black   -> 64-bit floating-point number
    # colour  -> 64-bit floating-point number
    dtype=[
        ('student', 'u8'),
        ('gender', 'S1'),
        ('black', 'f8'),
        ('colour', 'f8')
    ],

    # The values in the file are separated by commas.
    delimiter=',',

    # Treat the character 'X' as a missing value.
    #
    # Missing numeric values become np.nan by default.
    missing_values='X'
)

#========================================================================================================
print('\n')

print("Structured array:")
print(data)

print("\nArray data type:")
print(data.dtype)

print("\nStudent IDs:")
print(data['student'])

print("\nGender column:")
print(data['gender'])

print("\nBlack scores:")
print(data['black'])

print("\nColour scores:")
print(data['colour'])