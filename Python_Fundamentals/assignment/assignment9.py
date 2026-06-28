# sum of all digit of given number
num = int(input("enter number :"))

sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print(sum)    