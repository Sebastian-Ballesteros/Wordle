from urllib.request import urlopen
import random
import numpy as np

local_name = "Wordle_words"
punctuation = "&',.-()?1234567890"

def five_dict_create(url, word_length):
    words = []
    with urlopen(url) as fp:
        for line in fp:
            line = line.decode('utf-8-sig').strip("b'\n ")
            for p in punctuation:
                line = line.replace(p, "hello world")
            line = line.lower()
            if len(line) == word_length:
                words.append(line)
    return words

url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"

words = five_dict_create(url, 5)
game_word = random.choice(words)

for i in range(0, len(words)):
    words[i] = list(words[i])
words_array = np.array(words)
print(words_array)











