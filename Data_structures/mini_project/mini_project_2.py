# find runner up score

scores = [2, 3, 6, 6, 5]

# remove duplicate 
scores = list(set(scores))

#sort
scores.sort()

# runner up score
print(scores[-2])