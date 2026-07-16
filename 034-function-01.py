def star():
    for i in range(10):
        print('*' * i)

star()

# copy the function address
another_star=star

# it will call the anotherStar which has the sam code as the star function
another_star()


# =====================================================================================================
print('\n')


# define function with parameters
def get_avg(a, b):
    avg = (a + b)/2
    print("Average is:", avg)

get_avg(1,2)


# =====================================================================================================
print('\n')


# define function with args (arguments or list of parameters), use it when the number of parameters is unknown
def calc_avg(*numbers):
    print("Average is:", sum(numbers)/len(numbers))

calc_avg(1, 2, 3, 4, 5, 6, 7, 8, 9)

# you can set the parameters of a function to tuple like that:
nums = (9, 10)
get_avg(*nums)


# =====================================================================================================
print('\n')


def test_var_args(first_arg, second_arg, *other_args):
    print('First argument is:', first_arg)
    print('First argument is:', second_arg)
    print('Other arguments are:', other_args)

test_var_args('Ahmed', 'Mohamed', 'Abu Al-Saud', 30)


# =====================================================================================================
print('\n')


# define function with keyword arguements as parameters
def print_values(**values):
    print('Function parameters are:', values)

    # if the values is not empty
    if values is not None:
        for key, value in values.items():
            print('{} = {}'.format(key.ljust(10), value))

print_values(name='Ahmed', email='ahmed@gmail.com', age=30)

print('\n')

# you can set the parameters of a function to dictinary like that:
nums = {'a': 1, 'b': 2}
get_avg(**nums)


# =====================================================================================================
print('\n')


def show_details(a,b, *args, **kwargs):
    print('a is:', a)
    print('b is:', b)
    print('args are:', args)
    print('kwargs are:', kwargs)

# it will show:
# a is: 1
# b is: 2
# args are: (3, 4, 5, 6, 7, 8, 9)
# kwargs are: {}
show_details(1,2,3,4,5,6,7,8,9)

print('\n')

# it will show:
# a is: 1
# b is: 2
# args are: (3, 4, 5, 6, 7)
# kwargs are: {'c': 8, 'd': 9}
show_details(1,2,3,4,5,6,7,c=8,d=9)