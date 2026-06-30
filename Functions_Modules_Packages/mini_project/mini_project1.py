# sort colours
def sort_colours(colours):
    colour_list = colours.split("-")
    colour_list.sort()
    return "-".join(colour_list)

text = input("enter colours : ")
print(sort_colours(text))