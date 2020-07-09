# Exercise 1
def display_message(message):
    print(f"We are learning {message} in class.")


display_message("Python")


# Exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")


favorite_book("Harry Potter")


# Exercise 3
def make_shirt(*size, shirt_text="I love Python"):
    print(f"Shirt size: {size}\nText on shirt: {shirt_text}")


# make_shirt("S", "Jac is COOOOL")
# make_shirt(size="Small", shirt_text="Jackie rocks")
# make_shirt()
sizes = ["Medium", "Large"]
make_shirt(*sizes)

# Exercise 4
jacs_roomates = ["Jac", "Gabi", "Dennis", "Kobe", "Tom"]


def show_roommate(*args):
    for arg in args:
        make_great(arg)

def make_great(*args):
    for arg in args:
        print(f"{arg} the Great!")

show_roommate(*jacs_roomates)

# Exercise 5

def describe_city(city, country="Israel"):
    print(f"{city} is in {country}.")

describe_city('Tel Aviv')
describe_city('Haifa')
describe_city('Jerusalem')
describe_city('Haworth', country="United States")


# Exercise 6

def get_age(year, month, day):
    current_year = 2020
    current_month = 7





