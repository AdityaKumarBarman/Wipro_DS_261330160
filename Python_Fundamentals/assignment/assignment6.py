# given no is prime or not
num = int(input("enter number"))

if num <= 1:
    print("not prime")

else:
    is_prime = True

    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("prime number")
    else:
        print("not prime")        