# Exercise 1 

# Take three numbers from the user and print the greatest number.
# number1 = float(input("Enter your first number: "))
# number2 = float(input("Enter your second number: "))
# number3 = float(input("Enter your third number: "))
# if (number1 > number2) and (number1 > number3):
#    largest = number1
# elif (number2 > number1) and (number2 > number3):
#    largest = number2
# else:
#    largest = number3
# print("The largest number is",largest)


# Exercise 2 


letter = input("Enter a letter in the English alphabet: ")
if letter in ('a', 'e', 'i', 'o', 'u'):
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is not a vowel." )
    
# Exercise 3 


fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

# Exercise 4

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
list1.extend(list2)
print(list1)

# Exercise 7

import random
random_number = random.randint(1, 9)
print(random_number)
user_guesses = int(input("Guess a number from 1-9: "))
while user_guesses != random_number:
   user_guesses = int(input("Wrong number. Guess another number from 1-9: "))
print("Nice you got it!")

# Exercise 9

numbers= range(1,1000001)
print(min(numbers))
print(max(numbers))
print(sum(numbers))




