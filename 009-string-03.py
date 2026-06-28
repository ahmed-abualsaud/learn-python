a="  sweet home alabama sweet home alabama SWEET"

print('\n')

# partition() method splits the string into three parts: the part before the separator, the separator itself, and the part after the separator. It returns a tuple containing these three parts.
print("Partitioning the string using partition() method:", a.partition('home'))

# rpartition() method splits the string into three parts: the part before the separator, the separator itself, and the part after the separator. It returns a tuple containing these three parts.
# The difference between partition() and rpartition() is that partition() searches for the first occurrence of the separator, while rpartition() searches for the last occurrence of the separator.
print("Partitioning the string using rpartition() method:", a.rpartition('home'))

print('\n')

# The difference between find() and rfind() methods is that find() searches for the first occurrence of the specified substring,
# while rfind() searches for the last occurrence of the specified substring. Both methods return the index of the substring if found, or -1 if not found.
print("Finding the index of the first occurrence of 'home' in the string using find() method:", a.find('home'))
print("Finding the index of the first occurrence of 'home' in the string using rfind() method:", a.rfind('home'))


print('\n')

# The difference between index() and rindex() methods is that index() searches for the first occurrence of the specified substring,
# while rindex() searches for the last occurrence of the specified substring. Both methods return the index of the substring if found, 
# the difference between index(),rindex() and find(),rfind() is that index() and rindex() raise a ValueError if the substring is not found, 
# while find() and rfind() return -1.
print("Finding the index of the first occurrence of 'home' in the string using index() method:", a.index('home'))
print("Finding the index of the first occurrence of 'home' in the string using rindex() method:", a.rindex('home'))


print('\n')

print("Checking if the string starts with 'sweet' using startswith() method:", a.startswith('sweet'))
print("Checking if the string ends with 'alabama' using endswith() method:", a.endswith('alabama'))


print('\n')

print("Replacing 'home' with 'house' in the string using replace() method:", a.replace('home', 'house'))
print("Replacing 'home' with 'house' in the string using replace() method with count=1:", a.replace('home', 'house', 1))


print('\n')

print("Converting the string to uppercase using upper() method:", a.upper())
print("Converting the string to lowercase using lower() method:", a.lower())

print('\n')

# The difference between strip(), lstrip(), and rstrip() methods is that strip() removes whitespace from both the beginning and end of the string,
# lstrip() removes whitespace from the beginning of the string, and rstrip() removes whitespace from the end of the string. 
# All three methods return a new string with the whitespace removed, and the original string remains unchanged.
print("Stripping whitespace from the beginning and end of the string using strip() method:", a.strip())
print("Stripping whitespace from the beginning of the string using lstrip() method:", a.lstrip())
print("Stripping whitespace from the end of the string using rstrip() method:", a.rstrip())
print("Stripping 'T' from the beginning and end of the string using strip() method:", a.strip('T'))