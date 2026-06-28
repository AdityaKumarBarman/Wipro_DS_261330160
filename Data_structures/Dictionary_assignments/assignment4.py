# print key,values and both

d = {1:"apple", 2:"banana", 3:"mango"}

print("keys: ")
for key in d:
    print(key)

print("values: ")
for values in d.values():
    print(values)

print("keys and values: ")
for key,values in d.items():
    print(key,values)