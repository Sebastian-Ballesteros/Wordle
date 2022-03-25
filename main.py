from urllib.request import urlopen
import random

local_name = "Wordle_words"
punctuation = "&',.-()?1234567890"

def five_dict_create(url):
    words = []
    with urlopen(url) as fp:
        for line in fp:
            line = line.decode('utf-8-sig').strip("b'\n ")
            for p in punctuation:
                line = line.replace(p, "hello world")
            line = line.lower()
            if len(line) == 5:
                words.append(line)
    return words

url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"

words = five_dict_create(url)
game_word = random.choice(words)
print(game_word)







