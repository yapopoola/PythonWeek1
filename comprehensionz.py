# numbers = list(range(1, 11))
# squares = [num ** 2 for num in numbers]

# print(squares)


list_of_num1 = list(range(1, 21))
# print(list_of_num1)
list_of_num2 = []
 
for num in list_of_num1:
    if num % 2 == 0:
        list_of_num2.append(int(num / 2))
    elif num % 2 != 0:
        list_of_num2.append(int(num * 2))

even_list = [num / 2 for num in list_of_num1 if num % 2 == 0]
odd_list = [num * 2 for num in list_of_num1 if num % 2 != 0]

even_and_odd = [
    num / 2 if num % 2 == 0 
    else num * 2 if num % 2 != 0 
    else 0 
    for num in list_of_num1
]

print(even_and_odd)


'''
Create a list of numbers from 1 to 20 and then create
a set of those numbers where each number in the set
is each number in the list multiplied by 10
 '''

list_of_nums = list(range(1,21))
set_of_nums = set()
for every_num in list_of_nums:
    set_of_nums.add(every_num * 10)
print(set_of_nums)

set_comp = {every_num * 10 for every_num in list_of_nums}
print (set_comp)






student_info = {
    "Gabriella": 5,
    "Paul": 20,
    "Jack": 3,
    "Bond": 1,
    "Ahmed": 10,
    "Tiara": 2,
    "Kaitlyn": 6,
    "Lucy": 4
}

# students_activeness = student_info.copy()

# for student_name in students_activeness:
#     if students_activeness[student_name] > 5:
#         students_activeness[student_name] = 'active'
#     else:
#         students_activeness[student_name] = 'inactive'

# print(students_activeness)



# students_activeness = student_info.copy()

# for student_name, days_since_last_login in students_activeness.items():
#     if days_since_last_login > 5:
#         students_activeness[student_name] = 'active'
#     else:
#         students_activeness[student_name] = 'inactive'


students_activeness1 = {student_name:'active' if days_since_last_login > 5  else 'inactive'  for student_name, days_since_last_login in student_info.items() }
# {'Gabriella': 'inactive', 'Paul': 'active', 'Jack': 'inactive', 'Bond': 'inactive', 'Ahmed': 'active', 'Tiara': 'inactive', 'Kaitlyn': 'active', 'Lucy': 'inactive'}
active_students = {student_name:'active'  for student_name in students_activeness1 if students_activeness1[student_name] == 'active'}
inactive_students =  {student_name:'inactive'  for student_name in students_activeness1 if students_activeness1[student_name] == 'inactive'}

active_students_vR = {name: activeness for name, activeness in students_activeness1.items() if activeness == "active"}

actives = {}
for name, activeness in students_activeness1.items():
    if activeness == "active":
        actives[name] = activeness
print(actives)

# print(active_students)
# print(inactive_students)
# print(students_activeness1)



# print(student_info)

# students_activeness = {}

# for student_name in student_info:
#     if student_info[student_name] > 5:
#         students_activeness[student_name] = 'active'
#     else:
#         students_activeness[student_name] = 'inactive'

# print(students_activeness)
# # print(student_info)


# student_name : is_active
# print(days_since_last_login)