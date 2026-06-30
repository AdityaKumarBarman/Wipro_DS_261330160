# playing with names
def ispalindrome(name):
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")


def count_the_vowels(name):
    count = 0

    for ch in name:
        if ch in "aeiouAEIOU":
            count += 1

    print("No of vowels:", count)


def frequency_of_letters(name):
    d = {}

    for ch in name:
        if ch != " ":
            d[ch] = d.get(ch, 0) + 1

    print("Frequency of letters:")
    for key in d:
        print(key, "-", d[key])


name = input("Enter name: ")

ispalindrome(name)
count_the_vowels(name)
frequency_of_letters(name)