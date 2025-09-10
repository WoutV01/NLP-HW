import os
import re

def getCharDups(input):
    pattern = r"\b[a-zA-Z]*(?:a{3,}|e{3,}|i{3,}|o{3,}|u{3,})[a-zA-Z]*\b"
    return re.findall(pattern, input)

def collapse_vowels(input):
    result = re.sub(r'(a){2,}|(e){2,}|(i){2,}|(o){2,}|(u){2,}', lambda m: m.group(0)[0], input)
    return result

def count_words(input):
    counter = {}
    for word in input:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter

found_words_male = []
found_words_female = []

folder_path = './blogs'
for filename in os.listdir(folder_path):
    with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
        content = file.read()
        result = getCharDups(content)
        if filename[0] == "M":
            found_words_male.extend(result)
        else:
            found_words_female.extend(result)

collapsed_male = []
for word in found_words_male:
    collapsed_male.append(collapse_vowels(word.lower()))

counted_male = count_words(collapsed_male)
sorted_male = dict(sorted(counted_male.items(), key=lambda item: item[1], reverse=True))
print(sorted_male)
total_male = 0
for key in sorted_male:
    total_male += sorted_male[key]

collapsed_female = []
for word in found_words_female:
    collapsed_female.append(collapse_vowels(word.lower()))

counted_female = count_words(collapsed_female)
sorted_female = dict(sorted(counted_female.items(), key=lambda item: item[1], reverse=True))
print(sorted_female)

total_female = 0
for key in sorted_female:
    total_female += sorted_female[key]

print(total_male)
print(total_female)
