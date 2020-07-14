# Exercise 1
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age



cat1 = Cat("Jackie", "24")
cat2 = Cat("Cody", "10")
cat3 = Cat("Kobe", "1")



def biggest_cat(cat1,cat2,cat3):
    if cat1.age > cat2.age and cat1.age > cat3.age:
        return cat1
    elif cat2.age > cat1.age and cat2.age > cat3.age:
        return cat2
    else:
        return cat3

# big_cat = biggest_cat(cat1,cat2,cat3)
# print(big_cat.name + " is the biggest cat.")

# Exercise 2
class Dog:
    def __init__(self, nameDog, heightDog):
        self.nameDog = nameDog
        self.heightDog = heightDog

    def talk(self):
        print("woof")

    def jump(self):
        return self.heightDog * 2


def biggest_dog(dog1, dog2):
    if dog1.heightDog > dog2.heightDog:
        print(f"{dog1.nameDog} is the biggest")
    else:
        print(f"{dog2.nameDog} is the biggest")

davids_dog = Dog("Rex", 50)
davids_height = davids_dog.jump()
print(davids_height)
sarahs_dog = Dog("Teacup", 20)
sarahs_height = sarahs_dog.jump()
print(sarahs_height)

biggest_dog(davids_dog, sarahs_dog)

# Exercise 3
class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for lyric in self.lyrics:
            for word in lyric.split(" "):
                print(word)


happy_bday = Songs(["Have a sunshine on you,",
                   "Happy Birthday to you !"])
happy_bday.sing_me_a_song()

# Exercise 4


class Zoo:
    def __init__(self, zoo_names):
        self.name = zoo_names
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            return self.animals

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        print(f"Goodbye, {animal_sold}...")
        self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        print(self.animals)
        first_char = set(animal[0] for animal in self.animals)
        animal_pen = {}
        animals_index = 0
        for i in range(1, len(first_char) +1):
            animal[i] = []
            animal_pen[i].append(self.animals[animals_index])


ramat_Gan = Zoo("Ramat Gan")

ramat_Gan.add_animal("Lion")
ramat_Gan.add_animal("Tiger")
ramat_Gan.add_animal("Apes")

ramat_Gan.get_animals()

