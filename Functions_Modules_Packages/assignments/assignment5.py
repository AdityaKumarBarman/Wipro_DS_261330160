# print even numbers from list

def even_numbers(nums):
    even = []

    for i in nums:
        if i % 2 ==0:
            even.append(i)

    return even

list = [1,2,3,4,5,6,7,8,9]
print(even_numbers(list))          