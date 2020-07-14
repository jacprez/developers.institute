class Farm:

    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, number=1):
        if animal in self.animals.keys():
            self.animals[animal] += number
        else:
            self.animals[animal] = number

    def get_info(self):
        output = f"{self.name}'s Farm\n"
        for animal, amount in self.animals.items():
            space = " "*(20 - len(animal))
            output += f"{animal}{space}:{amount}\n"
        output += "   E-I-E-I-O   "
        return output



farm = Farm("MacDonald")
farm.add_animal("cow", 5)
farm.add_animal("sheep")
farm.add_animal("sheep")
print(farm.get_info())

