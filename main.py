from urllib.request import urlopen
import random
import numpy as np
from colorama import Fore

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

"""
game starts here
"""
game_word = list(game_word)
print(game_word)

count = 0
letters_in_word = ""
letters_not_in_word = ""
letters_in_word_and_place = []
while count < 5:
    guess = list(input(Fore.LIGHTWHITE_EX + 'Guess: '))
    print(Fore.LIGHTWHITE_EX + f'your guess was {guess}')
    if len(guess) != len(game_word):
        print('the word has too many/little letters')
        continue
    if guess == game_word:
        print(Fore.LIGHTGREEN_EX + 'correct word')
        break
    else: print(Fore.LIGHTWHITE_EX + 'still wrong word')

    for i in range(len(guess)):
        if guess[i] == game_word[i]:
            print(Fore.LIGHTGREEN_EX + guess[i])
            letters_in_word += guess[i]
            letters_in_word_and_place.append((guess[i], i))

        elif guess[i] in game_word:
            print(Fore.YELLOW + guess[i])
            letters_in_word += guess[i]
        else:
            print(Fore.RED + guess[i])
            letters_not_in_word += guess[i]

    count += 1
    if count == 5:
        print('you did not solve this in the 5 allowed attempts')
    print(set(letters_in_word), set(letters_not_in_word))

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
    print(len(pop_words) / len(words_array))
    try:
        words_array = np.delete(words_array, pop_words, axis=0)
        print(len(words_array))
    except:
        print("You typed the same letter twice")
        break











