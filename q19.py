def my_inappropriately_name_function(num):
    if num>1:
        my_inappropriately_name_function(num // 2)
    print(num%2, end='')

number = int(input("enter an integer"))
my_inappropriately_name_function(number)

"""
iteration 15//2 = 7
7//2 = 3
3//2 = 1
so 1, 3, 7, 15 three iteration with 4 times print 
print the binary for the input

"""