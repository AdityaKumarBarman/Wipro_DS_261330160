# given number is palindrome or not

original = int(input("enter no: "))

num = original
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("palindrome")
else:
    print("not palindrome")    