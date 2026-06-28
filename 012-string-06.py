import re
import numpy as np

a=','.join(('one','two','three'))

print('\n')

# The join() method is used to concatenate the elements of a list into a single string,
# with the specified separator (in this case, a comma) between each element.
print(a)


# Note here we used array instead of tuple
a=','.join(['one','two','three'])
print(a)

print('\n')

print(''.join(['one', 'two', 'three']))
print('\n'.join(['one', 'two', 'three']))


print('\n')


print(','.join([str(i) for i in np.random.randint(10, size=100)]))


print('\n')


print(f'my name is {"John"} and I am {25} years old')  # Using f-strings for string formatting
print('my name is %s and I am %d years old' % ('John', 25))  # Using the % operator for string formatting


print('\n')


print('my name is {} and I am {} years old'.format('John', 25))
print('my name is {:s} and I am {:d} years old'.format('John', 25))
print('my name is {0} and I am {1} years old'.format('John', 25))
print('my name is {first} and I am {last} years old'.format(first='John', last=25))


print('\n')

# It means that round pi to 3 digits after the decimal point
print('pi={0:.3f}'.format(np.pi))

# Add whitespace before and after the sentence passed to format() to display it in the middle. prefix whitespaces + sentence + postfix whitespaces = 30 (the number specified in the stirng)
print('|' + '{:^30}'.format('Hello World') + '|')

# is the string or the number of digits are lis than 10 it will add white spaces otherwise it will work like normal {0} or {1}
print('my name is {0:10} and I am {1:10d} years old'.format('John', 25))
