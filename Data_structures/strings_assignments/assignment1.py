# count upper and lower case letters

s = input("enter a string ")

upper = 0
lower = 0

for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print("upper case letter", upper)
print("lower case letter", lower)