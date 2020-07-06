# Exercise 1 

my_fav_numbers = set([6, 10, 63, 24])
print(my_fav_numbers)

my_fav_numbers.update([2, 96])
print(my_fav_numbers)

my_fav_numbers.pop()
print(my_fav_numbers)


friend_fav_numbers = set([12, 56, 20])
our_fav_numbers = friend_fav_numbers.union(my_fav_numbers)
print(our_fav_numbers)

# Exercise 4
numbers = range(1, 21)
for number in numbers:
    print(number)

# Exercise 5

userInput = input("Enter a topping to put on your pizza. Type 'quit' to exit. ")
while userInput != 'quit':
    print(f"Great, I'll add {userInput} to your pizza.")
    userInput = input("Enter another topping: ")

print('Exited.')

# Exercise 6

userAge = input("Enter your age. Type 'quit' to see your total. ")
family_cost = []
while userAge != 'quit':
    if int(userAge) < 3:
        userAge = input("Enter your age. Type 'quit' to see your total. ")
    elif int(userAge) < 12:
        family_cost.append(10)
        userAge = input("Enter your age. Type 'quit' to see your total. ")
    elif int(userAge) > 12:
        family_cost.append(15)
        userAge = input("Enter your age. Type 'quit' to see your total. ")

print(f"Your cost is: $ {sum(family_cost)}")

# Exercise 8

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)
apple_count = basket.count("Apples")
print(apple_count)
basket.clear()
print(basket)


# Exercise 9

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
while counter < len(my_list):
    print(my_list[-1 - counter])
    counter = counter + 1


# Exercise 10

jacs_list = [0, 1, 2, 3, 4, 5, 6]
counter = 0
while counter < len(jacs_list):
    if counter%2 == 0:
        print(f"{jacs_list[counter]} is an even index")
    counter += 1
