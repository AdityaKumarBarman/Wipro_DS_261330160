# people and facts

people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# display original dictionary
print("original dict:")
for name, fact in people.items():
    print(name , fact)

# change Jeff's fact
people["Jeff"] = "Is afraid of heights."

# add a new person
people["Jill"] = "Can hula dance."

print()
# display updated dictionary
print("updated dict:")
for name, fact in people.items():
    print(name , fact)