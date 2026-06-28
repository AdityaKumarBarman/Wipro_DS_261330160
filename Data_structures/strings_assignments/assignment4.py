# remove x from first or last

s = input("enter a string ")

if s.startswith("x"):
    s = s[1:]
if s.endswith("x"):
    s = s[:-1]
print(s)           