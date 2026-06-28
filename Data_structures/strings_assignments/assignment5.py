# repeat last n characters n times

s = input("enter a string: ")
n = int(input("enter n: "))

result = s[-n:] * n
print(result)