import os
import re

found_words = []
def getCharDups(input):
    pattern = r"\b[a-zA-Z](?:a{3,}|e{3,}|i{3,}|o{3,}|u{3,})[a-zA-Z]\b"
    return re.findall(pattern, input)

def collapse_vowels(input):
    result = re.sub(r'(a)\1+|(e)\2+|(i)\3+|(o)\4+|(u)\5+', lambda m: m.group(0)[0], input)
    return result

def count_words(input):
    counter = {}
    for word in input:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter

folder_path = './blogs'
for filename in os.listdir(folder_path):
    with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
        content = file.read()
        result = getCharDups(content)
        found_words.extend(result)

collapsed = []
for word in found_words:
    collapsed.append(collapse_vowels(word.lower()))

counted = count_words(collapsed)
sorted = dict(sorted(counted.items(), key=lambda item: item[1], reverse=True))
print(sorted)