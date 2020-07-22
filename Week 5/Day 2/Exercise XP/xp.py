class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, first_name, gender):
        new_member = {"name": first_name, "age": 0, "gender": gender, "is_child": True}
        self.members.append(new_member)
        print(f"Congrats {self.last_name} family on the new kid!")

    def is_18(self, name):
        for member in self.members:
            if name == member["name"]:
                if member["age"] > 18:
                    return True
                else:
                    return False

# TEST
test_family = Family([ {'name':'Michael','age':35,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False} ], "Smith")


test_family.born("Jackie", "Female")
for family in test_family.members:
    print(family["name"])

test_family.is_18("Jackie")

# Exercise 2

class TheIncredibles(Family):
    def __init__(self, members, last_name, power, incredible_name):
        super().__init__(members, last_name)
        self.power = power
        self.incredible_name = incredible_name
        for member in members:
            print(member)

incredible_family = test_family
    # def use_power(self):