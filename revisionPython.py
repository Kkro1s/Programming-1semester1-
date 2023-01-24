pi = 3.14
name = "CouchCoder"
num = 5
print(type(pi),type(name),type(num))
"""<class 'float'> <class 'str'> <class 'int'>"""

"""
type() function always return the class of the data type
"""

print(bool(1),bool(0))
"""True, False"""

# str1 = _
# print(str1,type(str1))
"""
_ underscore can not be variable,
"""

print(3+3==6 or 1+5==6)
"True"
print(3+3==6 and 1+5==6)
"True"
print(3+3==6 , 1+5==6)
"True True"
print(3+3==6 or 1+5==5)
"True"
print(3+3==6 and 1+5==5)
"Flase"
"""
and & or compares two sides variable
"""

q5 = 0
print(q5)
# num1+=1
# print(num1)
q5=+1
print(q5)
"""the += and =+ both make num increase by 1"""
# num1++
# print(num1)

q7_1 = 2**2
q7_2 = 2*2
print(q7_1 + q7_2)
""" 
8 ;  2x2 + 2^2 = 4 + 4 = 8
** is power
"""

namesq8 = ['mike','james','derrick']
namesq8.append('Ke')
print(namesq8)


print("abcdefg"[2])


user_input = "silly Strings"

q11 = 0
for s in user_input:
    q11+=1
print("c",q11,len(user_input))