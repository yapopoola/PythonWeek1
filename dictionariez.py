# Dictionaries are defined using the curly brackets as such. 
# The structure of dictionaries is key: value and dicts are unordered.
import pprint
participants = {
    1: "Rafihatu",
    2: 2,
    "students_first_names_list": ["Yusuf"],
    "students_last_names_tuple": ("Popoola",),
    200.75: "Is_it_price?",
    "image": "https:www.sdvdbjfgnkhf/fghfdsae.com",
    "class_info": {
        "teacher_first_name": "Rafihatu",
        "teacher_last_name": "Bello",
        "student_first_name": "Yusuf",
        "student_last_name": "Popoola",
        "number_of_classes_so_far": 5,
        "is_class_active": True,
        "num_of_missed_classes": None,
        "class_price": 1099.99,
        "is_class_large": False
    }
}
# pprint.pprint(participants)

# The keys of a dict must be unique and there are only two datatypes 
# that can serve as the key i.e. strings and numbers. The keys must be unique.
# Values in a dictionary can be any of the python's datatypes
# and values are accessed using their keys.
first_item = participants["students_first_names_list"]
class_info = participants["class_info"]
price = class_info["class_price"]
number_of_classes = class_info["number_of_classes_so_far"]

# The key names have to exist otherwise it throws an error
# You can use some of the dictionary methods such as .get(), .key(), .values()

# .get() gets the value based on the key provided and if no such key exists in the dict, 
# it returns None. If you specify a default value, 
# it returns the default instead of None if the key does not exist in the dict.
participants.get(0)  # -> None
participants.get(200.75)   # -> "Is_it_price?"
participants.get(0, "My default val")   # -> "My default val"

# Python dicts have a method called .keys() which returns a list of all the keys in that dict.
pprint.pprint(participants.keys())

# Python dicts have a method called .values()
pprint.pprint(participants.values())
 
# print("if no errors, this is printed after the earlier line.")
participants.