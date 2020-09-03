import json
# test dictonaries
dict = {
    "first": 1,
    "second": 2,
    "fourth": 4,
    "third":  3,
    "seventh":  7,
    "fifth":  5,
    "eigth":  8,
    "sixth":  6
}
dict2 = {
    "first": 3,
    "secound": 2,
    "third": 1
}
# actual variables
msg = "ruaghjdfjbhadfxjgraoifdj fdjkng sjd"
msg_frequency = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0
}

"""Functions"""
# returns the sorted frequencies


def frequency_sorter(dictonary):
    frequency_array = []
    for key in dictonary:
        frequency_array.append((key, dictonary[key]))
    sort(frequency_array)
    return frequency_array

# sorts with bubble sort recursively high to low seperate function so it can
# call on itself recursively


def sort(array):
    switches = 0
    for index in range(len(array)):
        if index + 1 < len(array):
            if array[index][1] < array[index + 1][1]:
                array.insert(
                    index + 2, (array[index][0], array[index][1]))
                array.pop(index)
                switches += 1
    if switches > 0:
        sort(array)

# finds the frequency of a string and updates to msg_frequency


def get_frequency(message):
    message = message.lower()
    for key in msg_frequency:
        for letter in message:
            if key == letter:
                msg_frequency[key] += 1

# compares one array frequency with the other and stores frequencies in order.


def frequency_matcher(real_values, coded_values):
    array_keys = []
    for i in real_values:
        array_keys.append((real_values[i][1], coded_values[i][1]))
    return array_keys


get_frequency(msg)
print(msg_frequency)
print(frequency_sorter(dict))
