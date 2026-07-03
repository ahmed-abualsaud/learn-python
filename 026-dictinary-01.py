print('\n')

# all keys must be from the same type, in this case all keys are strings and all values are strings too.
# keys are unique, which means you cannot have two keys with the same name in the same dictionary.
allKeys = {
    'egypt': '0020',
    'saudi arabia': '00966',
    'syria': '00963',
    'iraq': '00964',
    'jordan': '00962',
    'lebanon': '00961'
}

print(allKeys)

#==================================================================================================

print('\n')

dic1 = {i:i**2 for i in range(10)}

# print dictinary dic1 that contains the numbers from 0 to 9 as keys and their squares as values
print(dic1)

#==================================================================================================

print('\n')

# note all added keys must be from the same type, in this case all keys are strings and all values are strings too, and they must be unique
# also the new items added to the dictionary will be added at the end of the dictionary.
allKeys['egypt'] = '+0020' # you can change the value of a key in the dictionary by using the key name and assigning a new value to it.
allKeys['iraq'] = '+00964' # you can change the value of a key in the dictionary by using the key name and assigning a new value to it.
allKeys['lybia'] = '+00218' # you can add a new key to the dictionary by using a new key name and assigning a value to it.
allKeys['tunisia'] = '+00216' # you can add a new key to the dictionary by using a new key name and assigning a value to it.

print(allKeys)

#==================================================================================================

print('\n')

print('egypt' in allKeys) # it will print True because the key 'egypt' is in the dictionary allKeys
print('morocco' in allKeys) # it will print False because the key 'morocco' is not in the dictionary allKeys

print('\n')

print('+0020' in allKeys.values()) # it will print True because the value '+0020' is in the dictionary allKeys
print('0021' in allKeys.values()) # it will print False because the value '0021' is not in the dictionary allKeys