# sum of all numbers in a list

def list_sum(num):
    total = 0

    for i in num:
        total = total + i

    return total
my_list = [8,2,3,0,7]
print(list_sum(my_list))
    