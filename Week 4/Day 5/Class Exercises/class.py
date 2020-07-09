text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
#write a function that gives the number of words
#write a function that takes a letter, and counts the occurrances of that letter



def count_letter_occurances(string, letter):
    counter = 0
    for char in string:
        if letter == char:
            counter += 1
    return counter


def count_words(string):
    # return len(string.split())
    return count_letter_occurances(string, ' ') + 1
print(count_words(text))
print(count_letter_occurances(text, 'a'))