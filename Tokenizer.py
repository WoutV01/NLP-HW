import re

string = "Watching it, you'll cry your eyes 23 out."


def tokenizer(string):
    tokens = re.split(r'[\s\.,\']', string)
    return [token for token in tokens if token != ""]


print(tokenizer(string))
