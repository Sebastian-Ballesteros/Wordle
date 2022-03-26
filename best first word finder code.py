from urllib.request import urlopen
import random
import numpy as np

url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"


def five_dict_create(url, word_length):
    punctuation = "&',.-()?1234567890"
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


def words_array(words):
    for i in range(0, len(words)):
        words[i] = list(words[i])
    words_array = np.array(words)
    return words_array


def game(guess, game_word, words_array):
    letters_in_word = ""
    letters_not_in_word = ""
    letters_in_word_and_place = []

    if game_word == guess:
        return np.nan, len(range(1, words_array))

    for i in range(len(guess)):
        if guess[i] == game_word[i]:
            letters_in_word += guess[i]
            letters_in_word_and_place.append((guess[i], i))

        elif guess[i] in game_word:
            letters_in_word += guess[i]

        else:
            letters_not_in_word += guess[i]
    """
    Eliminating words from dictionary starts here
    """
    pop_words = []
    for word in range(0, len(words_array)):
        for i in letters_in_word:
            for n in letters_not_in_word:
                if i not in words_array[word] or n in words_array[word]:
                    pop_words.append(word)
        for letter, index in set(letters_in_word_and_place):
            if letter != words_array[word][int(index)]:
                pop_words.append(word)

    pop_words = np.unique(pop_words)
    try:
        words_array = np.delete(words_array, pop_words, axis=0)
    except:
        return np.nan, range(1, len(words_array))
    return words_array, pop_words


words = five_dict_create(url, 5)
words_array = words_array(words)
word_elimination_data = {}
words = five_dict_create(url, 5)

for word in words:
    avg_popped_words = []
    for iteration in range(0, 30):
        game_word = random.choice(words)
        words_array_short, popped_words = game(game_word, word, words_array)
        avg_popped_words.append(len(list(popped_words)))
    word_elimination_data[str(word)] = np.mean(avg_popped_words)
    print(word_elimination_data)
print(word_elimination_data)