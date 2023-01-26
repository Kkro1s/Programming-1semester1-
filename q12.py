import re
dob = 'Users Date of Birth is: 17/01/1975'
dob2 = '_-'
p = '\d+'
p2 = '.\w+'
p3 = '[\_-]{2}'
p4 = '{5}'
result = re.findall(p,dob)
result2 = re.findall(p3,dob2)
# result3 = re.findall(p4,dob2)
print(result,result2)


"""
Here are a few commonly used regular expressions in Python:

'\d'': Matches any digit (0-9).
'\w'': Matches any word character (a-z, A-Z, 0-9, _).
'\s'': Matches any whitespace character (space, tab, newline).
'.' : Matches any character except a newline
'^' : Matches the start of a string
'$' : Matches the end of a string
'[abc]' : Matches any character inside the square brackets (a, b, or c in this example)
'[a-z]' : Matches any character in the specified range (a through z in this example)
'\b'' : Matches a word boundary (the position between a word and a space)
'*' : Matches zero or more occurrences of the preceding character or group.
'+' : Matches one or more occurrences of the preceding character or group.
'?' : Matches zero or one occurrences of the preceding character or group.
Please note that this is not an exhaustive list, regular expressions can be used in many different ways.






"""