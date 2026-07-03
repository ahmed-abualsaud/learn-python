print('\n')

allKeys = {
    'egypt': '0020',
    'saudi arabia': '00966',
    'syria': '00963',
    'iraq': '00964',
    'jordan': '00962',
    'lebanon': '00961',
    'jordan': '+00962',
}

print(allKeys.get('egypt')) # it will print +0020 because the key 'egypt' is in the dictionary allKeys
print(allKeys['egypt']) # it will print +0020 because the key 'egypt' is in the dictionary allKeys
print(allKeys.get('jordan')) # it will print +00962 not 00962 because the key 'jordan' is douplicated in the dictionary allKeys and the last value assigned to the key 'jordan' is +00962
print(allKeys.get('morocco')) # it will print None because the key 'morocco' is not in the dictionary allKeys
print(allKeys.get('morocco', '00212')) # it will print '00212' because the key 'morocco' is not in the dictionary allKeys
# print(allKeys['morocco']) # it will raise an error because the key 'morocco' is not in the dictionary allKeys

#==================================================================================================

print('\n')

print("count:", len(allKeys)) # it will print 6 because there are 6 unique keys in the dictionary allKeys

#==================================================================================================

print('\n')

del allKeys['jordan'] # it will delete the key 'jordan' from the dictionary allKeys

print(allKeys)


allKeys.clear() # it will delete all keys from the dictionary allKeys

print(allKeys)


del allKeys # it will delete the dictionary allKeys itself, and if you try to print it after this line it will raise an error because the dictionary allKeys is deleted.

# print(allKeys) # this will raise an error because the dictionary allKeys is deleted

#==================================================================================================

print('\n')

allKeys = {
    'egypt': '0020',
    'saudi arabia': '00966',
    'syria': '00963',
    'iraq': '00964',
    'jordan': '00962',
    'lebanon': '00961',
    'jordan': '+00962',
}

newKeys = allKeys.copy() # it will create a new dictionary (deep copy) newKeys that contains the same keys and values as the dictionary allKeys

print(newKeys) # it will print the dictionary newKeys that contains the same keys and values as the dictionary allKeys

allKeys['morocco'] = '00212' # it will add a new key 'morocco' with value '00212' to the dictionary allKeys

print(newKeys) # it will print the dictionary newKeys that does not contain the key 'morocco' because it is a copy of the dictionary allKeys before the key 'morocco' was added to it
print(allKeys) # it will print the dictionary allKeys that contains the key 'morocco' because it was added to it after the copy was made

#==================================================================================================

print('\n')

set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

dic = dict.fromkeys(set) # it will create a new dictionary dic that contains the keys from the set and the value 'None' for each key

print(dic)

dic = dict.fromkeys(set, 'value') # it will create a new dictionary dic that contains the keys from the set and the value 'value' for each key

dic[1] = 'one' # it will change the value of the key 1 to 'one'
dic[2] = 'two' # it will change the value of the key 2 to 'two'
dic[3] = 'three' # it will change the value of the key 3 to 'three'

print(dic)