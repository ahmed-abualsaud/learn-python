for i in range(10):
    print("Hello, World!:", i) # this line will be printed 10 times with the value of i from 0 to 9 


print('\n')


for i in range(5, 10):
    print("Hello, World!:", i) # this line will be printed 5 times with the value of i from 5 to 9


print('\n')


for i in range(0, 10, 2):
    print("Hello, World!:", i) # this line will be printed 5 times with the value of i from 0 to 8 with a step of 2


print('\n')


print([(x,y) for x in range(5) for y in range(5) if x != y]) # this line will print a list of tuples with all combinations of x and y from 0 to 4 where x is not equal to y


print('\n')


for i in range(10):
    if i == 5:
        break # this line will break the loop when i is equal to 5
    print("Hello, World!:", i) # this line will be printed 5 times with the value of i from 0 to 4


print('\n')


for i in range(10):
    if i == 5:
        continue # this line will skip the rest of the loop when i is equal to 5
    print("Hello, World!:", i) # this line will be printed 9 times with the value of i from 0 to 9 except for 5


print('\n')


Y = 'supercalifragilisticexpialidocious'
for i in range(len(Y)):
    print(Y[i]) # this line will print each character of the string Y on a new line

print('\n')

z= ''
for i in range(len(Y)):
    z += Y[len(Y)-1-i] # this line will reverse the string Y and store it in z

print(z) # this line will print the reversed string z


print('\n')

countries = ['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina']
for country in countries:   
    print(country) # this line will print each country in the list countries on a new line


print('\n')


items = {'apple': 1, 'banana': 2, 'orange': 3}
for item in items:
    print(item) # this line will print each key in the dictionary items on a new line
for value in items.values():
    print(value) # this line will print each value in the dictionary items on a new line
for item in items.items():
    print(item) # this line will print each key-value pair in the dictionary items as a tuple on a new line


print('\n')


for i, v in enumerate(countries):
    print(i, v) # this line will print the index and value of each country in the list countries on a new line


print('\n')


for a, b in zip(countries, items):
    print(a, b) # this line will print the country and item key on a new line for each pair of countries and items


print('\n')


for i in range(10):
    print(i) # this line will print the value of i from 0 to 9 on a new line
else:
    print("Loop is over") # this line will be printed after the loop is over


print('\n')


print(sum([3*i**2 for i in range(10)])) # this line will print the sum of the squares of the numbers from 0 to 9
print(sum([3*i**2 for i in range(10) if i%2==0])) # this line will print the sum of the squares of the even numbers from 0 to 9
print(sum([3*i**2 for i in range(10) if i%2==0 and i%3==0])) # this line will print the sum of the squares of the even numbers from 0 to 9 that are also divisible by 3
print(sum([3*i**2 for i in range(10) if i%2==0 or i%3==0])) # this line will print the sum of the squares of the even numbers from 0 to 9 that are also divisible by 3 or 2
print(sum([3*i**2 for i in range(10) if not (i%2==0 or i%3==0)])) # this line will print the sum of the squares of the numbers from 0 to 9 that are not divisible by 2 or 3


print('\n')


print(sum([3*i**2 for i in [10*j for j in range(10)]])) # this line will print the sum of the squares of the numbers from 0 to 90 with a step of 10