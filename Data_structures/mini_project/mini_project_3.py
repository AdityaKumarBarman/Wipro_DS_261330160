# find the percentage

students = {
    "krishna": [67, 68, 69],
    "arjun": [70, 98, 63],
    "malika": [52, 56, 60]
}

name = input("enter student name: ")

# get marks
marks = students[name]

# calculate average
average = sum(marks) / len(marks)     # (67+68+69)/3

print("average percentage: ",average)