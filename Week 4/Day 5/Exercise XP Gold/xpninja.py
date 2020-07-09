
# Exercise 1

def findMax(*args):
    max = args[0]
    for arg in args:
        if arg > max:
            max = arg
    return max


print(findMax(*[1, 2, 3, 4]))

# Exercise 2

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number -1)

print(factorial(10))

