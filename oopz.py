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
    designed_by = "Rafi"

    def start_walking(where: str, start_from: str):
        ...

    def start_talking(): ...
        # raise NotImplementedError()


class HumanBeing:
    def __init__(self, eyes=2, hands=2, legs=2):
        self.number_of_eyes = eyes
        self.number_of_legs = legs
        self.number_of_hands = hands
        self.is_walking = None
        self._kidneys = 2

    def __start_walking(self, where: str, start_from: str):
        # start_leg = self.number_of_legs
        print(f"I have started walking using my {self.number_of_legs} legs.")
        # talk_as_i_walk = self.start_talking()
        # my_lips = self.lips
        # self.is_walking = True

    def start_talking(self):      
        print(f"I have started talking using my mouth and I am expressing myself with my {self.number_of_hands} hands.") 
        # self.lips = "1 pair"
        # walk = self.start_walking()
        # legs = self.number_of_legs

    def __str__(self):
        return f"I am a human being with {self.number_of_eyes} eye(s), {self.number_of_hands} hand(s), and {self.number_of_legs} leg(s)"

    # def __repr__(self):
    #     pass

# blind_man = HumanBeing()
blind_man = HumanBeing(hands=2, legs=2, eyes=0)
# blind_man.number_of_eyes
one_legged_woman = HumanBeing(eyes=2, hands=2, legs=1)
# one_legged_woman.start_talking()
# blind_man.number_of_eyes = 0

# print(f"Blind man currently has {blind_man._kidneys} functional kidneys")

# print("Blind man has started his deliverance and healing session...")
# blind_man.number_of_eyes = 2
# print("The blind man has been healed!!!")

# print(f"Blind man currently has {blind_man.number_of_eyes} eyes")

# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart


# x = Complex(3.0, -4.5)
# print(x.r, x.i)


# ---------------------------------INHERITANCE--------------------------------
class HumanBeing:
    def __init__(self, eyes=2, hands=2, legs=2):
        self.number_of_eyes = eyes
        self.number_of_legs = legs
        self.number_of_hands = hands
        self.is_walking = None

    def start_walking(self, where: str, start_from: str):
        # start_leg = self.number_of_legs
        print(f"I have started walking using my {self.number_of_legs} legs.")
        # talk_as_i_walk = self.start_talking()
        # my_lips = self.lips
        # self.is_walking = True

    def start_talking(self):      
        print(f"I have started talking using my mouth and I am expressing myself with my {self.number_of_hands} hands.") 
        # self.lips = "1 pair"
        # walk = self.start_walking()
        # legs = self.number_of_legs

    def __str__(self):
        return f"I am a human being with {self.number_of_eyes} eye(s), {self.number_of_hands} hand(s), and {self.number_of_legs} leg(s)"


class Male(HumanBeing): 
    def start_walking(self):
        print(f"Wo, me I am tired of walking with my {self.number_of_legs} legs o! I need to get a car.")

    def start_talking(self):
        print(f"To talk no tire you? My mouth, my {self.number_of_hands} hands and the rest of my body dey pain me abeg!")


class Female(HumanBeing): 
    def __init__(self, eyes=2, hands=2, legs=2, ears=2, nostrils=2, knees=2, genitalia="feminine"):
        self.number_of_knees = knees
        self.number_of_ears = ears
        self.nose = nostrils
        self.genitalia = genitalia
        super().__init__(eyes=eyes, hands=hands, legs=legs)


girl = Female(eyes=2, hands=2, legs=2, ears=2, nostrils=2, knees=21, genitalia="feminine")
boy = Male(2, 2, 2)

# boy.start_talking()
# boy.start_walking()
# print("The girl has genitalia with value:", girl.genitalia)

# ------------------------------MULTIPLE INHERITANCE-------------------------------
class Ship:
    def __init__(self):
        self.type = "ship"
        self.crew = 0
        self.max_passengers = 180
        self.was_serviced_recently = True
        self.captain = "Madam"

    def clean_the_property(self):
        return f"I have started cleaning the {self.type}"


class Hotel:
    def __init__(self):
        self.type = "hotel"
        self.crew = 100
        self.max_guests = 2000
        self.was_renovated_recently = False
        self.receptionist_of_the_day = "Ekaette"

    def clean_the_property(self):
        return f"I have started cleaning the {self.type}"


class CruiseShip(Hotel, Ship): 
    def __init__(self):
        Hotel.__init__(self)
        Ship.__init__(self)  


fishing_ship = Ship()
premier_hotel = Hotel()
tui_blue = CruiseShip()

# print("The type of fishing ship is:", fishing_ship.type)
# print("The type of premier is:", premier_hotel.type)
# print("The crew of tui_blue is:", tui_blue.clean_the_property())


class Hotel:
    def __init__(my, name, type, crew, guests, renovated, receptionist):
        my.name = name
        my.type = type
        my.crew = crew
        my.max_guests = guests
        my.was_renovated_recently = renovated
        my.receptionist_of_the_day = receptionist

    def clean_the_property(my):
        return f"I have started cleaning the {my.type}"

radisson = Hotel("Radisson", "4 star hotel", 20, 150, True, "Janet")
four_seasons = Hotel("Four Seasons", "5 star hotel", 100, 450, True, "Mark")

# print("Hi I am a hotel and my name is: ", radisson.name)
# print("Hi I am a hotel and my name is: ", four_seasons.name)

# radisson.name = "Blu"

# print("Hi I am a hotel and my name is: ", radisson.name)
# print("Hi I am a hotel and my name is: ", four_seasons.name)

my_hotels = [radisson, four_seasons, fishing_ship]

# for property in my_hotels:
#     print(property.clean_the_property())
    # if hotel.type == "5 star hotel":
    #     print(f"{hotel.name} welcomes you to the big leagues!")

    # else:
    #     print(f"{hotel.name} welcomes you to our 4 star hotel.")


# ------------------------------------- MULTI LEVEL INHERITANCE-----------------------------------
class Automobile:
    def __init__(self, seats, wheels, engine_type, fuel_type, transmission):
        self.number_of_seats = seats
        self.wheel_type = wheels
        self.engine = engine_type
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.minimum_speed = "2km/h"
        self.maximum_speed = "200km/h"
        # self.owner = HumanBeing()

    def get_parking_duration(self):
        if "back" in self.wheel_type:
            duration = "10 minutes"
        elif "front" in self.wheel_type:
            duration = "5 minutes"
        else:
            duration = "10 seconds"

        return duration     

class Car(Automobile): 
    def get_parking_duration(self):
        """Gets the amount of time it would take to park the vehicle depending on the type of wheels it has."""
        if "front" in self.wheel_type:
            return "It would take me 2 minutes to park properly"
        if "back" in self.wheel_type:
            return "It would take me 5 minutes to park properly"
        if "4" in self.wheel_type or "four" in self.wheel_type:
            return "Give me just 2 seconds and I am all done!"
        
    def get_time_between_speeds(self):
        def convert_speed_to_numerical_datatype(speed: str) -> int:
            speed_val = speed.split("km")[0]
            speed_val = int(speed_val)
            return speed_val
        
        min_speed = convert_speed_to_numerical_datatype(self.minimum_speed)
        max_speed = convert_speed_to_numerical_datatype(self.maximum_speed)

        return (max_speed - min_speed) // 10
        
class SportsCar(Car): 
    def __init__(self, seats, wheels, engine_type, fuel_type, transmission):
        super().__init__(seats, wheels, engine_type, fuel_type, transmission)
        self.minimum_speed = "60km/h"
        self.maximum_speed = "1000km/h"
    

    def get_time_between_speeds(self):
        return super().get_time_between_speeds() // 10

nissan_racer = SportsCar(2, "four wheel drive", "v8", "gasoline", "automatic")
# print(nissan_racer.get_time_between_speeds())


# ------------------------------------- STATIC METHODS IN OOP-----------------------------------
class Car(Automobile): 
    def get_parking_duration(self):
        """Gets the amount of time it would take to park the vehicle depending on the type of wheels it has."""
        if "front" in self.wheel_type:
            return "It would take me 2 minutes to park properly"
        if "back" in self.wheel_type:
            return "It would take me 5 minutes to park properly"
        if "4" in self.wheel_type or "four" in self.wheel_type:
            return "Give me just 2 seconds and I am all done!"

    @staticmethod  
    def convert_speed_to_numerical_datatype(speed: str) -> int:
            speed_val = speed.split("km")[0]
            speed_val = int(speed_val)
            return speed_val
        
    def get_time_between_speeds(self):
        min_speed = Car.convert_speed_to_numerical_datatype(self.minimum_speed)
        max_speed = Car.convert_speed_to_numerical_datatype(self.maximum_speed)
        return (max_speed - min_speed) // 10

    
# Car().convert_speed_to_numerical_datatype()


class RECTANGLE:
    name = "Rectangle"

    def number_of_sides(self):
        print("I have 2 sides")
    
    # @classmethod
    # def info_class_name(cls):
    #     return cls.name
    
    @classmethod
    def change_name_class(cls, new_name):
        cls.name = new_name

    # def change_name_instance(self, new_name):
    #     self.name = new_name


# rafi_rectangle = RECTANGLE()
# yusuf_rectangle = RECTANGLE()

# print("I am Rafi's rectangle, my name is: ", rafi_rectangle.name)
# print("I am Yusuf's rectangle, my name is: ", yusuf_rectangle.name)

# yusuf_rectangle.change_name_class("Latest Version 2")

# print("I am Rafi's rectangle, my name is: ", rafi_rectangle.name)
# print("I am Yusuf's rectangle, my name is: ", yusuf_rectangle.name)

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError(f"area method must be implemented")

    @abstractmethod
    def perimeter(self): 
        raise NotImplementedError(f"perimeter method must be implemented")

    @abstractmethod
    def volume(self): 
        raise NotImplementedError(f"volume method must be implemented")

    @abstractmethod
    def number_of_sides(self): 
        raise NotImplementedError(f"number_of_sides method must be implemented")


class Rectangle(Shape):
    def number_of_sides(self):
        print("I have 2 sides")

    def area(self, length, breadth):
        return length * breadth


class Triangle(Shape): ...

my_shape = Shape()
# rafi_triangle = Triangle()
# rafi_rectangle = Rectangle()
# print(rafi_rectangle)
