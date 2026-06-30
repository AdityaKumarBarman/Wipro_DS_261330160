# count uppercase and lower case letters

def count_letters(text):
    upper = 0
    lower = 0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("upper ",upper)
    print("lower", lower)

count_letters("HelloWorld")