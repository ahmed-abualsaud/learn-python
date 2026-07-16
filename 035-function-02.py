# set a default value for the function parameters
def powers(n, p = 1):
    print('{} power {} = {}'.format(n, p, n**p))

powers(2) # it will print 2 power 1 = 2 because the default value of p is 1
powers(2, 2) # it will print 2 power 2 = 4


# =====================================================================================================
print('\n')


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue') :
    print ( "-- This parrot wouldn't", action)
    print ("if you put", voltage, "volts through it.")
    print ("-- Lovely plumage, the", type)
    print ("-- It's", state, "!")

parrot(1000) # 1 positional argument
parrot(voltage=1000) # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM') # 2 keyword arguments

# worng function call
# parrot() # required argument missing
# parrot(voltage=5.0, 'dead') # non-keyword argument after a keyword argument
# parrot(110, voltage=220) # duplicate value for the same argument
# parrot(actor='John Cleese') # unknown keyword argument


# =====================================================================================================
print('\n')

# example on function return, it will return the b'th power of number a
def powers(a, b):
    return a**b

print('3 power 2 =', powers(3,2))

def add7(a):
    return a + 7

def times4(a):
    return a * 4

# the returned value from the powers function is 8
# then 8 will enter the times4 function so the output will be 32
#finally 32 will enter the add7 function so the output will be 39
print(add7(times4(powers(2,3))))


# =====================================================================================================
print('\n')


xx=3

def local_func():
    xx=4

local_func()

# it will print 3 because the variable xx inside the function is a function-scope variable so it can not be seen from outside the function
print(xx)

def global_func():
    global xx # allow the function to access the global scope variables like xx
    xx=5

global_func()

# it will print 5 not 3 because the keyword global allow the function to access the global scope variables like xx
print(xx)

# =====================================================================================================
print('\n')


# an example of the lambda function
powers = lambda a,b : a**b

print(powers(5,2)) # 5^2 = 25


powers = [lambda x: 1, lambda x: x, lambda x: x**2, lambda x: x**3]

print(powers[0](5))  
print(powers[1](5))  
print(powers[2](5))  
print(powers[3](5))
