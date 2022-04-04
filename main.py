import random
import numpy as np
from colorama import Fore
from words import Wordle_words

words = Wordle_words[:]


def words_array(lst):
    ar = lst[:]
    for i in range(0, len(ar)):
        ar[i] = list(ar[i])
    return np.array(ar)


def game(guess, game_word, words_array):
    letters_in_word = []
    letters_not_in_word = ""
    letters_in_word_and_place = []

    for i in range(len(guess)):
        if guess[i] == game_word[i]:
            letters_in_word_and_place.append((guess[i], i))

        elif guess[i] in game_word:
            letters_in_word.append((guess[i], i))

        else:
            letters_not_in_word += guess[i]
    """
    Eliminating words from dictionary starts here
    """
    pop_words = [0]
    for word in range(0, len(words_array)):
        """If the letters are not in the guess word, discard words that contain that letter"""
        for i in letters_not_in_word:
            if i in words_array[word]:
                pop_words.append(word)
                break

        if word == pop_words[-1]:
            continue

        for letter, index in set(letters_in_word):
            """discard words that do not have a letter in guess word"""
            if letter not in words_array[word]:
                pop_words.append(word)
                break

            """discard words that have a letter in word but not in the right place, in the same place as guess word"""
            if letter == words_array[word][int(index)]:
                pop_words.append(word)
                break

        if word == pop_words[-1]:
            continue

        "discard letters that don't have the right letter in the right place"
        for letter, index in set(letters_in_word_and_place):
            if letter != words_array[word][int(index)]:
                pop_words.append(word)
                break

    pop_words = np.unique(pop_words)
    words_array = np.delete(words_array, pop_words, axis=0)

    return words_array, pop_words


"""
game starts here
"""
words_array = words_array(words)
game_word = random.choice(words)
game_word = list(game_word)
print(game_word)

count = 0
letters_in_word = []
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
            letters_in_word_and_place.append((guess[i], i))

        elif guess[i] in game_word:
            print(Fore.YELLOW + guess[i])
            letters_in_word.append((guess[i], i))
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

    pop_words = [0]
    for word in range(0, len(words_array)):
        """If the letters are not in the guess word, discard words that contain that letter"""
        for i in letters_not_in_word:
            if i in words_array[word]:
                pop_words.append(word)
                break

        if word == pop_words[-1]:
            continue
        for letter, index in set(letters_in_word):
            """discard words that do not have a letter in guess word"""
            if letter not in words_array[word]:
                pop_words.append(word)
                break

            """discard words that have a letter in word but not in the right place, in the same place as guess word"""
            if letter == words_array[word][int(index)]:
                pop_words.append(word)
                break

        if word == pop_words[-1]:
            continue

        "discard letters that don't have the right letter in the right place"
        for letter, index in set(letters_in_word_and_place):
            if letter != words_array[word][int(index)]:
                pop_words.append(word)
                break

    pop_words = np.unique(pop_words)
    words_array = np.delete(words_array, pop_words, axis=0)
    words = np.delete(words, pop_words)

    word_elimination_data = {}

    n = 1
    for word in words:
        avg_popped_words = []
        words_array_short, popped_words = game(game_word, word, words_array)
        avg_popped_words.append(len(list(popped_words)))

        word_elimination_data[str(word)] = np.mean(avg_popped_words)
        n += 100
    print(len(pop_words))
    print(sorted(word_elimination_data.items(), key=lambda item: item[1], reverse=True))

