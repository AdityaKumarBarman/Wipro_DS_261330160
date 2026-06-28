miles = float(input("how far would you like to travel in miles: "))

if miles < 3:
    print("you should ride a bicycle")
elif miles >= 3 and miles < 300:
    print("you should ride a motorcycle") 
else:
    print("drive a supercar")       