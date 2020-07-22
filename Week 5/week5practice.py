fruits = ["apple", "orange", "grapes", "banana"]
# Slicing lists
# print(fruits[0:2])
# for fruit in fruits:
    # print(fruit[3::])

fruits[0:1] = "newfruit"
# print(fruits)


store = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US" : ["pink", "green"]
        }
}

# Objects
x = 5
y = 'string'

# Classes

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hi I am", self.name, "and I am", self.age, "years old.")

    def talk(self):
        print('Bark')


class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def talk(self):
        print("meow")

tim = Cat('tim', 5, 'blue')
# tim.speak()
# tim.talk()


class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = self.gas + 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas

class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print("BEEP BEEP")


class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

    def beep(self):
        print("HONK HONK")



vehicle1 = Vehicle(1000, 10, "Black")
vehicle1.fillUpTank()
# print(vehicle1.gas)

# print(vehicle1.gasLeft())

car1 = Car(2000, 5, 'Blue', 120)
# car1.beep()



class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y +p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, p):
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __lt__(self, p):
        return self.length() < p.length()

    def __le__(self, p):
        return self.length() <= p.length()

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'



p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)
p5 = p1 + p2
p6 = p4 - p1
p7 = p2*p3

# print(p5, p6, p7)
# print(p1 == p2)
# print(p4 < p5)

# Intermediate Python

# Option Parameters
# Parameter: anything in the parenthesis in a function

def func(x):
    return x **2

call = func(5)
print(call)

# Collections
# Containers: data type or object that stores multiple objects (i.e. list, tuple, set, dict <= 4 main ones)

# counter is another type of container

from collections import Counter

c = Counter('gallad')
print(c)
c = Counter(['a', 'a', 'b', 'c', 'c'])
print(c)

c = Counter({'a': 1, 'b':2})
print(c)
