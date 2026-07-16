numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = list(filter(lambda x : x%2, numbers))
print(odd_numbers)

even_numbers = list(filter(lambda x: not x%2, numbers))
print(even_numbers)

greater_than_5 = list(filter(lambda x: x>5, numbers))
print(greater_than_5)

squared_numbers = list(map(lambda x : x**2, numbers))
print(squared_numbers)

def powers(a, b):
    return a**b

power_3 = list(map(lambda x : powers(x, 3), numbers))
print(power_3)


# =====================================================================================================
print('\n')


# act as an iterator every time you call the function it send you the next value of i then pause.
def yield_func():
    for i in range(10):
        yield i

y = yield_func()

print(next(y)) # return 0
print(next(y)) # return 1
print(next(y)) # return 2


# =====================================================================================================
print('\n')


def read_huge_file(file_path):
    # 'with' ensures that the file will close automatically after we finish.
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip() # We send the line and pause the function.


# We specify the path to the large file (imagine its size is 10 GB, for example).
large_file_path = "data/huge_data_log.txt"

# This loop will read line by line "on request"
for log_line in read_huge_file(large_file_path):
    # We perform the processing we want on this line only.
    if "ERROR" in log_line:
        print(f"We find the error: {log_line}")

# Once the cycle is complete, the old line is deleted from memory. 
# The function wakes up, reads the next line, and calculates the yield, and so on.


# =====================================================================================================
print('\n')


# return the first n numbers of fibonacci
def fibonacci(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a+b
    return result

n = 10
print("First {} numbers in fibonacci seris are:".format(n), fibonacci(n))


# =====================================================================================================
print('\n')


# an example of febonacci function that returns fibonacci number generater using yield keyword, you call the function only n times
def fibonacci_yield(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for i in fibonacci_yield(5):
    print('Fibonacci number', i)


# =====================================================================================================
print('\n')


# and exmaple of a recursive function (a function that calls itself)
def factorial(n):
    return n * factorial(n-1) if n > 1 else 1 # note that the recursive functions must have a default value that returnd when a confition happens, default value here is 1

# you can also write the factorial like this
def fac(n):
    if n ==1 : 
        return 1
    else : 
        return n * fac(n-1)

n=5
print('Factorial of {} is:'.format(n), factorial(n), fac(n))