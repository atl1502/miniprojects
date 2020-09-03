import random
msg = """hello this is a test of the message scrambling"""

# returns scrambled alphabet and I was too lazy to convert into array


def alphabet_randomizer():
    alphabet_str = "abcdefghijklmnopqrstuvwxyz"
    alphabet_list = []
    for letter in alphabet_str:
        alphabet_list.append(letter)
    random.shuffle(alphabet_list)
    return alphabet_list


# returns a scrambled message


def scrambler(msg):
    key_dict = {}
    coded_msg = ""
    original_alphabet = alphabet_randomizer()
    coded_alphabet = alphabet_randomizer()
    for i in range(len(original_alphabet)):
        key_dict[original_alphabet[i]] = coded_alphabet[i]
    for charater in msg:
        letter_use = False
        for key in key_dict:
            if charater == key:
                coded_msg += key_dict[key]
                letter_use = True
                break
        else:
            coded_msg += charater
    return coded_msg


print(scrambler(msg))
