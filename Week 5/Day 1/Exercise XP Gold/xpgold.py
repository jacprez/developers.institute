# Exercise 1
from math import pi

class Circle:
    def __init__(self, radius = 1.0):
        self.radius = radius

    def compute_perimeter(self):
        circum = 2 * pi * self.radius
        return circum

    def compute_area(self):
        area = pi * (self.radius ** 2)
        return area


# circle_1 = Circle(10)
# circle_1_perimeter = circle_1.compute_perimeter()
# print(circle_1_perimeter)
# circle_1_area = circle_1.compute_area()
# print(circle_1_area)


# Exercise 2

import random

class MyList:
    def __init__(self, nonempty_list):
        self.nonempty_list = nonempty_list
        if not self.nonempty_list or not isinstance(nonempty_list, list):
            print("doesnt work")


    def reverse_list(self):
        self.nonempty_list.reverse()
        return self.nonempty_list

    def random_list(self):
        empty_list = []
        for i in range(len(self.nonempty_list)):
            empty_list.append(random.randint(1,20))
        return empty_list




number_list = [1,2,3,4,5,6,7,8,9,10]
my_list = MyList(number_list)
my_list.reverse_list()
print(my_list.random_list())

# Exercise 3

class QuantumParticle:
    def __init__(self):
        self.position = random.randint(1,10000)
        self.momentum = random.uniform(0, 1)
        self.spin = random.choice([-0.5, 0.5])

    def get_position(self):
        old_position = self.position
        self.disturbance()
        return old_position

    def get_momentum(self):
        old_momentum = self.momentum
        self.disturbance()
        return old_momentum

    def get_spin(self):
        return self.spin

    def disturbance(self):
        self.position = random.randint(1, 10000)
        self.momentum = random.uniform(0, 1)






#TESTING
test = QuantumParticle()
print(test.get_momentum())
print(test.momentum)