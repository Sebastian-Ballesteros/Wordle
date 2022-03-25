from colorama import Fore

game_word = 'hello'
game_word = list(game_word)
print(game_word)

count = 0
letters_in_word = ""
letters_not_in_word = ""
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

