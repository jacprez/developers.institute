l = [1, 2, 3, 4]
def even_numbers(my_list):
    evens = []
    for num in my_list:
        if num%2==0:
            evens.append(num)
    return evens


evenNum = even_numbers(l)
print(evenNum)

# List comprehension with same problem

a_list = [1, 2, 3, 4]
def is_even(num):
    return num % 2 == 0
def even_nums(l):
    evens = [num for num in l if is_even(num)]
    return evens

print(even_nums(a_list))


def my_name(name):
    first, last = name.split(" ")
    return first, last

name = my_name("Jackie Prezant")
print(name)

