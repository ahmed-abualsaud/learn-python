a="sweet home alabama sweet home alabama SWEET"

print('\n')

print("Counting the number of occurrences of 'home' in the string using count() method:", a.count('home'))

print('\n')

# The difference between title() and capitalize() methods is that title() capitalizes the first letter of each word in the string, while capitalize() capitalizes only the first letter of the entire string and makes the rest of the characters lowercase.
print("Converting the string to title case using title() method:", a.title())
print("Capitalizing the first character of the string using capitalize() method making the rest lowercase:", a.capitalize())
# The swapcase() method returns a new string with all uppercase letters converted to lowercase and all lowercase letters converted to uppercase. The original string remains unchanged.
print("Swapping the case of the string using swapcase() method:", a.swapcase())


print('\n')

# The center() method returns a new string that is centered within a specified width. The original string is padded with spaces on both sides to achieve the desired width.
print("Centering the string with width 50 using center() method:", a.center(50))
print("Centering the string with width 50 and padding character '-' using center() method:", a.center(50, '-'))

print('\n')

# The ljust() and rjust() methods return a new string that is left-justified or right-justified within a specified width, respectively. The original string is padded with spaces on the right or left side to achieve the desired width.
print("Adjusting the string to the left with width 50 using ljust() method:", a.ljust(50))
print("Adjusting the string to the right with width 50 using rjust() method:", a.rjust(50))
print("Adjusting the string to the left with width 50 and padding character '-' using ljust() method:", a.ljust(50, '-'))
print("Adjusting the string to the right with width 50 and padding character '-' using rjust() method:", a.rjust(50, '-'))


print('\n')

print("Filling the string with width 50 and padding character '0' using zfill() method:", a.zfill(50))


print('\n')

print("Checking if the string is alphanumeric using isalnum() method:", a.isalnum())
print("Checking if the string is alphabetic using isalpha() method:", a.isalpha())


print('\n')

# The difference between isdecimal(), isdigit(), and isnumeric() methods is that isdecimal() checks if all characters in the string are decimal characters (0-9),
# isdigit() checks if all characters in the string are digits (0-9, superscripts, subscripts, and other digit characters), and isnumeric() checks if all characters 
# in the string are numeric characters (0-9, superscripts, subscripts, fractions, Roman numerals, and other numeric characters). In general, isdecimal() is the most strict, 
# while isnumeric() is the most lenient. If a string contains only decimal characters, it will return True for all three methods. If a string contains only digit characters, 
# it will return True for isdigit()
print("Checking if the string is decimal using isdecimal() method:", a.isdecimal())
print("Checking if the string is a digit using isdigit() method:", a.isdigit())
print("Checking if the string is numeric using isnumeric() method:", a.isnumeric())

print('\n')

# The difference between isidentifier() and istitle() methods is that isidentifier() checks if the string is a valid identifier (i.e., it can be used as a variable name in Python),
# while istitle() checks if the string is in title case (i.e., the first letter of each word is capitalized). If a string is a valid identifier, it will return True for isidentifier(), 
# regardless of whether it is in title case or not. If a string is in title case, it will return True for istitle(), but it may not be a valid identifier.
print("Checking if the string is a valid identifier using isidentifier() method:", a.isidentifier())
print("Checking if the string is in title case using istitle() method:", a.istitle())


print('\n')

# The difference between isupper() and islower() methods is that isupper() checks if all characters in the string are uppercase letters, while islower() checks if all characters in 
# the string are lowercase letters. If a string contains only uppercase letters, it will return True for isupper(), regardless of whether it contains lowercase letters or not. If a string 
# contains only lowercase letters, it will return True for islower(), but it may not be in uppercase.
print("Checking if the string is in uppercase using isupper() method:", a.isupper())
print("Checking if the string is in lowercase using islower() method:", a.islower())


print('\n')

# The difference between isprintable() and isspace() methods is that isprintable() checks if all characters in the string are printable (i.e., they can be displayed on the screen),
# while isspace() checks if all characters in the string are whitespace characters (i.e., spaces, tabs, newlines, etc.). If a string contains only printable characters, it will return
# True for isprintable(), regardless of whether it contains whitespace or not. If a string contains only whitespace characters, it will return True for isspace(), but it may not be printable.
print("Checking if the string is printable using isprintable() method:", a.isprintable())
print("Checking if the string is whitespace using isspace() method:", a.isspace())