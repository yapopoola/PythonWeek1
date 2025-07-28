# Strings can be defined using single quotes as below
student_name = 'Yusuf Popoola'

# Strings can be defined using double quotes as below
teacher_name = "Rafihatu Bello"

# Strings can be spread into multiple lines using three of either double or single quotes as below
class_description = '''
    This is just a small example.
    The student is here.
    The teacher is also here.
'''

"""
In Python, a clean way of breaking really long lines of code is to break it down into more lines.
These lines should be written within a parenthesis `()` 
to let python know that it should be treated as one line.  
"""
encapsulated_string = (
    "This is aunty B"
    "This is also uncle B"
    "Madam C dey here o"
    "UNcle C too dey"
)

# We can add two or more strings together using the plus sign to form a new string.
combined_string = (
    "The teacher's name is:" + " " +
    teacher_name + " " +
    "while the student's name is:" + " " +
    student_name
)

# We can also combine strings together using the string method called `.format`
teacher_and_student = "The teacher's name is: {} while the student's name is: {}".format(teacher_name, student_name)

# You can combine string using the `f` prefix to indicate to python that it is a formatted string.
teacher_and_student_new_format = (
    "The teacher's name is: "
    f"{teacher_name} "
    "while the student's name is: "
    f"{student_name}"
)

# You can cause a string to be repeated multiple times by multiplying 
multiplied_student_name = f"{student_name} \n" * 4

# String indexing is when you want to view specific parts of your string.
# Indexes in Python start from 0 until the last character in the string.
# To access the characters from the end of the string, you use the minus sign before the index.
first_char = teacher_and_student[0]
last_char = teacher_and_student[-1]

# Getting the length of a string.
length_of_student_name = len(student_name)

# String slicing allows you use the index of a string to determine 
# where you want your string to start and stop.
student_first_name = student_name[0:5:3]
student_last_name = student_name[6:]

# print(student_first_name)

# Accessing attributes of strings using dot notation
teacher_and_student = "The teacher's name is: {} while the student's name is: {}".format(teacher_name, student_name)
password = "7a"

# print(student_name.replace(student_name[6:], "*****"))


"""
Assignment: create a variable called `word` 
and then create another variable called `reversed_word`.
Reversed word should be the word in reverse using string slicing e.g
word = "mango" 
reversed_word = {This is the part you should implement using slicing}
print(word) --> mango
print(reversed_word) --> ognam
"""

word = "rafihatu"
reversed_word = word[: : -1]

print(reversed_word)
