a="sweet home alabama"
multiline_string = """This is a multiline string.
It can span multiple lines.
It is enclosed in triple quotes."""

print('\n')

print("Length of the string is:", len(a))
print("List of characters in the string:", list(a))
print("Sorted list of characters in the string:", sorted(list(a)))
print("Reversed list of characters in the string:", list(reversed(a)))
print("Set of characters in the string is:", set(a))
print("Split the string into a list of words:", a.split())
print("Split the string by character e:", a.split('e'))
print("Multiline string:", multiline_string.splitlines())