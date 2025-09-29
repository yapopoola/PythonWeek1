# A class defines what an object should look like, and an object is created based on that class. For example:

list_1 = [2, 5, 8, 23, 6, 99]
list_2 = [3, "Rafi", 99, "100", "random words", 234, 247]

str_1 = "I am a sentence".replace(" ", "")
str_2 = "Am I a question?".replace(" ", "")

# print(type(list_1))

class HumanBeing: 
    number_of_eyes = 2
    number_of_legs = 2
    number_of_hands = 2

    def start_walking(where: str, start_from: str):
        ...

    def start_talking(): ...
        # raise NotImplementedError()

# class HumanBeing:
#     def __init__(self):
#         number_of_eyes = 2
#         number_of_legs = 2
#         number_of_hands = 2


# class Male(HumanBeing): ...

# class Female(HumanBeing): ...

blind_man = HumanBeing()
# blind_man.start_walking()
one_legged_woman = HumanBeing()
# one_legged_woman.start_talking()
blind_man.number_of_eyes = 0

print(HumanBeing.number_of_eyes)