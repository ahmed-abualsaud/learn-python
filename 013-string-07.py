# import regular expression library
import re

print('\n')

# extract all emails from a string using python regular expression library
email1 = re.compile(r'\w+@\w+\.[a-z]{1}')
text = "To email Guido, try guido@python.org or guido@google.com "
print(email1.findall(text))


print('\n')


email2=re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')
text = "To email Guido, try guido@python.org or guido@google.com "
print(email2.findall(text))


print('\n')


email3=re.compile(r'(?P<user>[\w.]+)@(?P<domain>\w+).(?P<suffix>[a-z]{3})')
text = "To email Guido, try guido@python.org or guido@google.com "
match=email3.match('guido@python.org')
print(match.groupdict())
