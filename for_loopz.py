# For loops on strings.
sentence = "This is our new class where we lear about loops!"
new_string = ""
for each_char in sentence: 
    new_char = each_char + "o "
    new_string = new_string + new_char
    
# print(new_string)


# For loops on lists
prices = [59.99, 79.99, 89.99, 23.75, 42.45, 57.75, 100.0]
new_prices = []

for price in prices:
    discount = round(price * 0.25, 2)
    if discount > 10:
        discount = 10
    new_price = round(price - discount, 2)
    new_prices.append(new_price)


# For loops in tuples
ages = (18, 20, 21, 7, 40, 8, 55, 60, 15, 23, 12, 14, 16)
can_I_sell_to_them = {}

for age in ages:
    if age >= 18:
        valid_age = True
    else:
        valid_age = False

    can_I_sell_to_them[age] = valid_age

# print(can_I_sell_to_them)


students = {"Yusuf", "Pops", "Brenda", "Bellz", "Jamie", "Pops", "Jack", "Diana"}
student_groups_by_alphabet = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "J": [],
    "Y": [],
    "Others": []
}

for student in students:
    if student.startswith("A"):
        student_groups_by_alphabet["A"].append(student)
    elif student.startswith("B"):
        student_groups_by_alphabet["B"].append(student)
    elif student.startswith("C"):
        student_groups_by_alphabet["C"].append(student)
    elif student.startswith("D"):
        student_groups_by_alphabet["D"].append(student)
    elif student.startswith("J"):
        student_groups_by_alphabet["J"].append(student)
    elif student.startswith("Y"):
        student_groups_by_alphabet["Y"].append(student)
    else:
        student_groups_by_alphabet["Others"].append(student)


# Looping through a dictionary.
# Remove key value pairs where the value is empty
dict_items = student_groups_by_alphabet.copy().items()

for key, value in dict_items:
    if len(value) == 0:
        student_groups_by_alphabet.pop(key)

print(dict_items)
print("-----------------------------------------------")
print(student_groups_by_alphabet)
# print(f"Key {key} has {len(value)} items which are {value}")
