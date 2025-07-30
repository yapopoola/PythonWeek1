# Sets are defined using the curly brackets as such.
participants = {"Yusuf", "Popoola", "Yusuf", "Rafihatu", "Yusuf", "Bello"}
set_of_participants = set(participants)

# Sets cannot contain duplicate values and they are unordered.
# print(participants)

# You can add more items to a set
participants.add("yusuf")

# We can combine two sets together either by using the pipe `|` or the union method.
non_participants = {"Git", "Python", "VSCode", "Github", "Yusuf", "Bello"}
# all_participants = participants.union(non_participants)
all_participants = participants | non_participants

# We can get the common factors between two sets .
# intersect = participants.intersection(non_participants)
intersect = participants & non_participants
# print(intersect)

# We can get the difference between two sets using 
# either the difference method or the minus sign.
set_difference = non_participants.difference(participants)
set_difference = participants - non_participants
# print(set_difference)

# You can clear your set using the `clear` method.
all_participants.clear()
print(all_participants)
