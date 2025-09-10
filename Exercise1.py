import nltk
from nltk.stem import PorterStemmer

ps = PorterStemmer()

word_types = []

with open("sorted_types_HW1.txt") as f:
    for word in f:
        lemma = ps.stem(word.strip())
        if lemma not in word_types:
            word_types.append(lemma)

print(len(word_types))
print(word_types)
