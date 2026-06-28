# import operating system library
import os

# import shell utility library
import shutil as su

# 'w' means open the file for write only, It will create the file if it does not exist. 
f = open('./data/file-handling.txt', 'w')

# It will remove the old content of the file and fill the file with the new contnet
# if you did not add \n at the end of the string, the two strings will be concatinated together at the same line
f.write('this is the first line\n')
f.write('this is the second line')

f.close()

#==================================================================================================

f = open('./data/file-handling.txt', 'a')

# Append this text to the end of this file
f.write('\nthis is the third line')

f.close()

#==================================================================================================

print('\n')

# if the file does not exists it will throw a file does not exists error
f = open('./data/file-handling.txt', 'r')

content = f.read()

print(content)

f.close()

#==================================================================================================

print('\n')

# if the file does not exists it will throw a file does not exists error
f = open('./data/file-handling.txt', 'r')

# print it line by line
for row in f:
    print(row)

f.close()

#==================================================================================================

f = open('./data/file-handling.csv', 'w')

f.write('first line\n')
f.write('second line\n')
f.write('third line\n')

f.close()

#==================================================================================================

f = open('./data/file-handling.xls', 'w')

f.write('first line\n')
f.write('second line\n')
f.write('third line\n')

f.close()

#==================================================================================================

print('\n')
path='./data/test-folder-creation'

# exist_ok = True means if the folder exists, delete it and creat a brand new empty folder.
# exist_ok = False means if the folder exists, throw an exception.
new_folder = os.makedirs(path, exist_ok = True)

if os.path.exists(path):
    print('Folder: {0} created successfully'.format(path))

current_working_directory = os.getcwd()

print(current_working_directory)

#==================================================================================================

print('\n')

# Copy one file
su.copyfile('./data/file-handling.txt', './data/test-folder-creation/file-handling.txt')

# Copy the ./data/test-folder-creation folder to the current folder
su.copytree('./data/test-folder-creation', './test-folder-creation')

# Move the file ./data/file-handling.csv to the current directory, you can use it to move folders as well.
su.move('./data/file-handling.csv', './file-handling.txt')