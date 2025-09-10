import os
import re

found_words_female = []
found_words_male = []

def getCharDups(input):
    pattern = r"\b[a-zA-Z]*(?:a{3,}|e{3,}|i{3,}|o{3,}|u{3,})[a-zA-Z]*\b"
    return re.findall(pattern, input)

def collapse_vowels(input):
    vowel = None

    def replaceDups(m):
        nonlocal vowel
        vowel = m.group(0)[0]
        return vowel

    result = re.sub(r'(a){2,}|(e){2,}|(i){2,}|(o){2,}|(u){2,}', replaceDups, input)
    return (vowel, result)

def count_words(input):
    counter = {}
    for word in input:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter

folder_path = './blogs'
print(len(os.listdir(folder_path)))
for filename in os.listdir(folder_path):
    with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
        content = file.read()
        result = getCharDups(content)
        if filename[0] == 'F':
            found_words_female.extend(result)
        elif filename[0] == 'M':
            found_words_male.extend(result)

collapsed_female = {'a': {}, 'e': {}, 'i': {}, 'o': {}, 'u': {}}
for word in found_words_female:
    vowel, result = collapse_vowels(word.lower())
    if result in collapsed_female[vowel]:
        collapsed_female[vowel][result] += 1
    else:
        collapsed_female[vowel][result] = 1

for key in collapsed_female:
    items = collapsed_female[key].items()
    sorted_dict = dict(sorted(items, key=lambda item: item[1], reverse=True))
    collapsed_female[key] = sorted_dict
    print(collapsed_female[key])

collapsed_male = {'a': {}, 'e': {}, 'i': {}, 'o': {}, 'u': {}}
for word in found_words_male:
    vowel, result = collapse_vowels(word.lower())
    if result in collapsed_male[vowel]:
        collapsed_male[vowel][result] += 1
    else:
        collapsed_male[vowel][result] = 1

for key in collapsed_male:
    items = collapsed_male[key].items()
    sorted_dict = dict(sorted(items, key=lambda item: item[1], reverse=True))
    collapsed_male[key] = sorted_dict
    print(collapsed_male[key])