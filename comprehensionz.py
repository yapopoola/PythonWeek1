# numbers = list(range(1, 11))
# squares = [num ** 2 for num in numbers]

# print(squares)


list_of_num1 = list(range(1, 21))
print(list_of_num1)
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
