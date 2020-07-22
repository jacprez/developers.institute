# Exercise 1
class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True
    my_cats = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Cat.my_cats.append(self.name)

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    # def __init__(self, name, age, sounds):
    #     super().__init__(name, age)
    #     self.sounds = sounds

    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    # def __init__(self, name, age, sounds):
    #     super().__init__(name, age)
    #     self.sounds = sounds

    def sing(self, sounds):
        return f'{sounds}'

class AnotherBreed(Cat):
    # def __init__(self, name, age, sounds):
    #     super().__init__(name, age)
    #     self.sounds = sounds

    def sing(self, sounds):
        return f'{sounds}'


bengal1 = Bengal('Jackie', 24)
another_breed1 = AnotherBreed('Kali', 1)
chartreux1 = Chartreux('Becca', 24)


print(another_breed1.sing('Ruff'))
print(Cat.my_cats)
my_pets = Pets(Cat.my_cats)
print(animal.walk for animal in my_pets.animals)

print(pet.walk for pet in my_pets.animals)
print(my_pets.walk)


# Exercise 2
class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance += deposit_amount

    def withdraw(self, withdrawal_amount):
        if self.balance > withdrawal_amount:
            self.balance -= withdrawal_amount
        else:
            print("Insufficient funds.")


class Owner(BankAccount):
    def __init__(self, owner, balance, credit_card_number, password):
        super().__init__(owner, balance)
        self.credit_card_number = credit_card_number
        self.password = password

    def check_owner_info(self):
        for i in range(2):
            ccn = int(input("Credit card number: "))
            passw = input("Password: ")
            if self.password == passw:
                answer = input("Do you want to deposit or withdraw? ")
                if answer == 'deposit':
                    money = int(input("Money: "))
                    self.deposit(money)
                    return
                elif answer == 'withdraw':
                    money = int(input("Money: "))
                    self.withdraw(money)
                    return
                else:
                    print("I don't understand.")
            else:
                print("wrong password.")

