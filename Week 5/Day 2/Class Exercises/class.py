class Human():
    # gets all basic parameters of each instance
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.eyes_color = "blue"
    def talk(self):
        print(f"{self.name}: bla bla bla....")
hayim = Human(name="Hayim", age=25, gender="M")
print(hayim.name)
print(hayim.age)
print(hayim.eyes_color)
hayim.eyes_color = "green"
print(hayim.eyes_color)
hayim.talk()
class American(Human):
    def amazed(self):
        print("It's amazing !")
class Latino(American):
    pass
tsivia = American(name="Tsivia", age=22, gender='F')
print(tsivia.name)
tsivia.talk()
tsivia.amazed()




class Book:
    BEST_AUTHOR = "Victor Hugo"
    def __init__(self, text, title, author, genre):
        self.text = text
        self.title = title
        self.author = author
        self.genre = genre
    def read(self):
        sentences = self.text.split(". ")
        for s in sentences:
            print(s)
hp = Book(text="some sentences. some other sentences about the dursleys.",
          title="Harry Potter", author="J.K. Rowling", genre="Fantasy")
hp.read()  # read(hp)
print(hp.BEST_AUTHOR)
print(Book.BEST_AUTHOR)


class Student:

    def __init__(self, name, school, major):
        self.name = name
        self.school = school
        self.major = major

    def set_gpa(self, gpa):
        self.gpa = gpa

    def compute_gpa(self, grades):
        self.gpa = sum(grades) / len(grades)


class Teacher:
    def __init__(self, name, school, discipline):
        self.name = name
        self.school = school
        self.discpline = discipline
    def teach(self):
        print(f"You don't understand nothing about {self.discpline}...")
# PhdStudent class inherits from student
# add a new attribute called supervisor (the name of the Phd supervisor)


class PhdStudent(Student, Teacher):
    def __init__(self, name, school, major, supervisor, discipline):
        Student.__init__(self, name, school, major)
        Teacher.__init__(self, name, school, discipline)
        self.supervisor = supervisor
albert = PhdStudent(name="Albert", school="Stanford", major="Physics", supervisor="Max",
                    discipline="Relativity")
albert.compute_gpa([90, 89, 98, 78])
print(albert.gpa)
albert.teach()