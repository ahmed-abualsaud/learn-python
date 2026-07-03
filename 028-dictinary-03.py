print('\n')

grades = {
    'ahmed': 90,
    'mohamed': 80,
    'ali': 70,
    'sara': 60,
    'fatma': 50,
    'hassan': 40
}

print(grades) # it will print the dictionary grades that contains the keys and values of students and their grades

print('\n')

print(grades.keys()) # it will print the keys of the dictionary grades that contains the names of students

print(grades.values()) # it will print the values of the dictionary grades that contains the grades of students

print(grades.items()) # it will print the view object that displays a list of a dictionary's key-value tuple pairs

print('\n')

print(list(grades.keys())) # it will print the list of keys of the dictionary grades that contains the names of students

print(list(grades.values())) # it will print the list of values of the dictionary grades that contains the grades of students

print(list(grades.items())) # it will print the list of key-value tuple pairs of the dictionary grades

print('\n')

print(tuple(grades.keys())) # it will print the tuple of keys of the dictionary grades that contains the names of students

print(tuple(grades.values())) # it will print the tuple of values of the dictionary grades that contains the grades of students

print(tuple(grades.items())) # it will print the tuple of key-value tuple pairs of the dictionary grades

print('\n')

print(set(grades.keys())) # it will print the set of keys of the dictionary grades that contains the names of students

print(set(grades.values())) # it will print the set of values of the dictionary grades that contains the grades of students

print(set(grades.items())) # it will print the set of key-value tuple pairs of the dictionary grades

#==================================================================================================

print('\n')

data = {
    'ahmed': (90, 'A'),
    'mohamed': (80, 'B'),
    'ali': (70, 'C'),
    'sara': (60, 'D'),
    'fatma': (50, 'E'),
    'hassan': (40, 'F')
}

print(data)

data['ahmed'] = [90, 'A+'] # it will update the value of the key 'ahmed' in the dictionary data to be a list instead of a tuple

print(data) # it will print the dictionary data that contains the keys and values of students and their grades, and the value of the key 'ahmed' is updated to be a list instead of a tuple

print(data['ali'][1]) # it will print the second element of the value of the key 'ali' in the dictionary data, which is 'C'

del data['fatma'] # it will delete the key 'fatma' from the dictionary data

print(data) # it will print the dictionary data that contains the keys and values of students and their grades, and the key 'fatma' is deleted from it