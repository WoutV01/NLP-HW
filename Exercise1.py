import nltk
from nltk.stem import WordNetLemmatizer
nltk.download("wordnet")
nltk.download("omw-1.4")
import spacy

wnl = WordNetLemmatizer()

word_types = []

with open("sorted_types_HW1.txt") as f:
    for word in f:
        lemma = wnl.lemmatize(word.strip())
        if lemma not in word_types:
            word_types.append(lemma)

print(len(word_types))
print(word_types)

word_types = []
nlp = spacy.load("en_core_web_sm")
lemmatizer = nlp.get_pipe("lemmatizer")
with open("sorted_types_HW1.txt") as f:
    doc = nlp(f.read())
    for token in doc:
        if token.lemma_ not in word_types:
            word_types.append(token.lemma_)
        else:
            print(str(token) + " -> " + str(token.lemma_))

print(len(word_types))
print(word_types)
