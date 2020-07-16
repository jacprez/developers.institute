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
jacs_roommates = ["Jac", "Gabi", "Dennis", "Kobe", "Tom"]


def show_roommate(roommate_list):
    for roommate in roommate_list:
        print(roommate)

def make_great(roommate_list):
    for index in range(len(roommate_list)):
        roommate_list[index] = roommate_list[index] + " the great."
    return roommate_list


show_roommate(jacs_roommates)
print(make_great(jacs_roommates))

# Exercise 5

def describe_city(city, country="Israel"):
    print(f"{city} is in {country}.")

describe_city('Tel Aviv')
describe_city('Haifa')
describe_city('Jerusalem')
describe_city('Haworth', country="United States")


# Exercise 6


user_input = input("Enter the year and month you were born to see if you can retire (i.e. YYYY/MM): ")
user_birthdate = user_input.split('/')
user_year = int(user_birthdate[0])
user_month = int(user_birthdate[1])

def get_age(year, month):
    current_year = 2020
    current_month = 7
    age = current_year - year
    if current_month < month:
        age -= 1
    return age




gender = input("Enter your gender M or F: ")
def can_retire(gender, age):
    if gender == "M" and age >= 67:
        return "Male retire"
    elif gender == "F" and age >= 62:
        return "Female retire"
    else:
        return "You are too young to retire."

print(can_retire(gender, get_age(user_year, user_month)))





