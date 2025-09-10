import os
import re

found_words = []

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
        found_words.extend(result)

collapsed = {'a': {}, 'e': {}, 'i': {}, 'o': {}, 'u': {}}
for word in found_words:
    vowel, result = collapse_vowels(word.lower())
    if result in collapsed[vowel]:
        collapsed[vowel][result] += 1
    else:
        collapsed[vowel][result] = 1

for key in collapsed:
    items = collapsed[key].items()
    sorted_dict = dict(sorted(items, key=lambda item: item[1], reverse=True))
    collapsed[key] = sorted_dict
    print(collapsed[key])