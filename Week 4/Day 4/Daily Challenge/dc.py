matrix = [
    [7, '', 3],
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', '', '#'],
    ['s', 'M', ''],
    ['$', 'a', ''],
    ['#', 't', '%'],
    ['i', 'r', '!']
]

text = ''
for col in range(3):
    for row in matrix:
        char = row[col]
        if type(char) is str and char.isalpha():
            text += char
        else:
            text += ' '


print(text)