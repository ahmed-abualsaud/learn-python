# \n is used to create a new line in the string. When the string is printed, the text after \n will appear on a new line.
print('I am in the first line\nI am in the second line')

# note the backslash before the single quote and double quote characters in the string. 
# The backslash is used to escape the special meaning of these characters, 
# allowing them to be included in the string without causing a syntax error.
print('This is a string that contains a single quote character: \'. It also contains a double quote character: ".')


print('\n')

# The backslash is used to escape the special meaning of the backslash character itself, allowing it to be included in the string without causing a syntax error.
print('C:\\Users\\Username\\Documents\\file.txt')

# The r prefix before the string indicates that it is a raw string, which means that backslashes are treated as literal characters and not as escape characters.
print(r'C:\Users\Username\Documents\new_file.txt')

# The \t is used to create a tab space in the string. When the string is printed, the text after \t will be indented by a tab space.
print('This is a string \t separated by tab')


print('\n')


multiple_lines_string1 = '''This is a string that spans multiple lines. 
It can be used to create multi-line strings in Python.
This is the third line of the string.'''

multiple_lines_string2 = """This is another string that spans multiple lines.
It can also be used to create multi-line strings in Python.
This is the fourth line of the string."""

# You can use either triple single quotes (''') or triple double quotes (""") to create multi-line strings in Python.
print(multiple_lines_string1)
print(multiple_lines_string2)


print('\n')


print('first string' 'second string')  # Concatenation of two string literals
print('first string' + 'second string')  # Concatenation of two string literals using the + operator
print('first string', 'second string')  # Concatenation of two string literals with a space in between


print('\n')


print('first string', end='')  # Concatenation of two string literals without a space in between
print('second string', end='')  # Concatenation of two string literals without a space in between
print('third string')  # Concatenation of two string literals without a space in between


print('\n')


print('my name is %s and I am %5d years old' % ('John', 25))  # Use number after % to specify the minimum width of the field. In this case, the age will be right-aligned in a field of width 5.
print('my name is %s and I am %05d years old' % ('John', 25))  # Use number after % to specify the minimum width of the field. In this case, the age will be right-aligned in a field of width 5 and padded with zeros on the left.
print('my name is {:<10} and I am {:>5} years old'.format('John', 25))  # Use < and > to specify left and right alignment, respectively. In this case, the name will be left-aligned in a field of width 10
print(f'my name is {"John":<10} and I am {25:>5} years old')  # Use < and > to specify left and right alignment, respectively.