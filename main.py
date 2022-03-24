from urllib.request import urlopen
import random
url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
local_name = "Wordle_words"
punctuation = "&',.-()?1234567890"
words = []
with urlopen(url) as fp:
    for line in fp:
        line = line.decode('utf-8-sig').strip("b'\n ")
        for p in punctuation:
            line = line.replace(p, "hello world")
        line = line.lower()
        if len(line) == 5:
            words.append(line)

game_word = words[random.randint(0, len(words))]

print(game_word)





