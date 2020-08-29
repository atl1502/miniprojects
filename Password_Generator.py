import random
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
             "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase = []
for letter in lowercase:
    uppercase.append(letter.upper())

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_characters = ["!", "@", "#", "$", "%", "^",
                      "&", "*", "(", ")", "[", "]", "|", "-", "_"]


def generate(length):
    if length < 6:
        return "password is weak try longer password"
    password = ""
    character_type_list = []
    rules = True
    for num in range(length):
        character_type = random.randint(1, 4)
        character_type_list.append(character_type)
        if character_type == 1:
            password += lowercase[random.randint(0, 25)]
        elif character_type == 2:
            password += uppercase[random.randint(0, 25)]
        elif character_type == 3:
            password += numbers[random.randint(0, 9)]
        elif character_type == 4:
            password += special_characters[random.randint(0, 14)]
    for num in [1, 2, 3, 4]:
        if num not in character_type_list:
            rules = False
    if rules:
        return password
    else:
        return generate(length)


print(generate())
