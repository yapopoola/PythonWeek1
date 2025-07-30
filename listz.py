# Lists are one of the numerous ways in python to hold multiple items in one container.
# It can hold the different datatypes in the same list.
participants = ["Yusuf", 1, "Rafihatu", 2, "Popoola", "Bello", 3.5, True]

# A list can contain other lists inside of it e.g.
participants = [["Yusuf", 1, "Rafihatu",], 2, ["Popoola", "Bello",], 3.5, "Python"]

# List indexing happens using the bracket notation and the value of the item's index.
participants_first_names = participants[0][0]

# To get the length of a list
list_size = len(participants[0])

# To get a sublist of a list, we use slicing based on the indexes we want
# based on list_name[start: stop: step]
reversed_list = participants[0][::-1]

# You can add lists together using extend.
first_names = ["Yusuf", "Rafihatu",]
last_names = ["Popoola", "Bello",]

# Extend takes in another sequence and adds all 
# the items in that sequence into the list whose extend function was called.
first_names.extend(last_names)
first_names = first_names + last_names
# Append takes in just one item and makes it the last item 
# in the list whose append function was called.
last_names.append(first_names)

# Explore other functions of the list
new_list = [
    "Yusuf", "Bello", "Rafihatu", "Yusuf", "Popoola", "Yusuf"
]
# Sort would sort string based lists alphabetically and number based list based on their values.
new_list.sort()
# Reverse would simply return the list starting from the last item to the first item.
new_list.reverse()
print(new_list)
