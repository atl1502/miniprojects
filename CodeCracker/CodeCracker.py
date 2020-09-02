import json
message = ""
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


def frequency_sorter(dictonary):
    frequency_array = []
    for key in dictonary:
        frequency_array.append((key, dictonary[key]))
    sort(frequency_array)
    print(frequency_array)


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


frequency_sorter(dict)
