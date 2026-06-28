# print true if they have same last digit

def last_digit(a,b):
    if(a % 10 == b % 10):
        return True
    else:
        return False

print(last_digit(7,17))
print(last_digit(6,17))
print(last_digit(3,113))
