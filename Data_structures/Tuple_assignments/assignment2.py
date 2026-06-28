# wap to check element exists in a tuple or not

t = (10, 20, 30, 40, 50)

item = int(input("Enter the element to search: "))

# check if the element exists
if item in t:
    print("element exists")
else:
    print("not")