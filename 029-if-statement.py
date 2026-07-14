print('\n')

if True:
    print("This is true") # this line will be printed because the condition is true

if False:
    print("This is false") # this line will not be printed because the condition is false

#==================================================================================================

print('\n')

if 5 > 3:
    print("5 is greater than 3") # this line will be printed because the condition is true

if 5 < 3:
    print("5 is less than 3") # this line will not be printed because the condition is false

#==================================================================================================

print('\n')

if 5 == 3:
    print("5 is equal to 3") # this line will not be printed because the condition is false

if 5 != 3:
    print("5 is not equal to 3") # this line will be printed because the condition is true

#==================================================================================================

print('\n')

if 5 >= 3:
    print("5 is greater than or equal to 3") # this line will be printed because the condition is true

if 5 <= 3:
    print("5 is less than or equal to 3") # this line will not be printed because the condition is false

#==================================================================================================

print('\n')

if 5 > 3 and 5 < 10:
    print("5 is greater than 3 and less than 10") # this line will be printed because both conditions are true

if 5 > 3 and 5 > 10:
    print("5 is greater than 3 and greater than 10") # this line will not be printed because the second condition is false

#==================================================================================================

print('\n')

if 5 > 3 or 5 < 10:
    print("5 is greater than 3 or less than 10") # this line will be printed because the first condition is true

if 5 > 3 or 5 > 10:
    print("5 is greater than 3 or greater than 10") # this line will be printed because the first condition is true

#==================================================================================================

print('\n')

if not (5 < 3):
    print("5 is not less than 3") # this line will be printed because the condition is true

#==================================================================================================

print('\n')

if 5 > 3:
    print("5 is greater than 3") # this line will be printed because the condition is true
else:
    print("5 is not greater than 3") # this line will not be printed because the condition is false

#==================================================================================================

print('\n')

# note and = & , or = | , not = ~ but it is deprecated and should not be used, instead use not
if 5 < 3 | 5 == 3:
    print("5 is less than 3") # this line will not be printed because the condition is false
elif 5 == 3 & 5 > 3: # elif stands for else if
    print("5 is equal to 3") # this line will not be printed because the condition is false
else:
    print("5 is greater than 3") # this line will be printed because the condition is true

#==================================================================================================

print('\n')

if 5 > 3: print("5 is greater than 3") # this line will be printed because the condition is true
elif 5 == 3: print("5 is equal to 3") # this line will not be printed because the condition is false
else: print("5 is less than 3") # this line will not be printed because the condition is false

#==================================================================================================

print('\n')

a,b = 11,10
max = a if a>b else b # it will assign the value of a to max if the condition (a>b) is true, otherwise it will assign the value of b to max
print (max)

#==================================================================================================

print('\n')

a,b = 11,10
min = a if a<b else b # it will assign the value of a to min if the condition (a<b) is true, otherwise it will assign the value of b to min
print (min)