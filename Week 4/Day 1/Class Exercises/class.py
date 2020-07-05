msg = "Hello World"
print (msg)

# In the python shell, Create a variable called `my_age`, use python to know how old you will be in 123879 years


age = 23
my_age = age + 123879
print(my_age)

# Write a program that prints the numbers from 1 to 100 inclusive
# But for multiples of three print fizz instead of the number
# For the multiples of five print Buzz.
# For numbers which are multiples of both three and five print FizzBuzz instead.

for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("fizz")
    elif i%5 == 0:
        print("buzz")
    else:
        print(i)
    
    