# we can define string using single quotes or double quotes
a1="sweet home alabama"
a2='sweet home alabama'


print('\n')
print(a1)
print(a2)

print('\n')
print('=========================================================')
print('\n')

# characters numbering starts from 0
print("first character in the string is:", a1[0])
print("second character in the string is:", a1[1])
print("third character in the string is:", a1[2])
print("ninth character in the string is:", a1[8])
print("last character in the string is:", a1[-1])
print("second last character in the string is:", a1[-2])
print("third last character in the string is:", a1[-3])
print("ninth last character in the string is:", a1[-9])
print("first three characters in the string are:", a1[0:3])
print("first three characters in the string are:", a1[:3])
print("characters from 3 to 8 in the string are:", a1[3:8])
print("characters from 3 to the end of the string are:", a1[3:])
print("characters from -8 to -3 in the string are:", a1[-8:-3])
print("reverse of the string is:", a1[::-1])
print("characters from 3 to 8 in the string with step 2 are:", a1[3:8:2])
print("characters from 3 to the end of the string with step 2 are:", a1[3::2])
print("repeating the string 3 times gives:", a1*3)
print("concatenating the string with ' is a song' gives:", a1 + " is a song")
print("character at index -100 in the string is:", a1[-100])
print("character at index 100 in the string is:", a1[100])
