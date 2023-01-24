dob = (12,10,1989)
print(dob)
validate = input("is this?")

if 'n'in validate or 'N' in validate:
    print("reset")
    # dob[0] = 0
    # dob[1] = 0
    # dob[2] = 0
print(dob[0],dob[1],dob[2])