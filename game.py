game_word = 'carlo'
game_word = list(game_word)
print(game_word)

while True:
    guess = list(input('Guess: '))
    print(f'your guess was {guess}')

    if guess == game_word:
        print('correct')
        break
    else: print('still wrong word')

    for i in range(len(guess)):
        if guess[i] == game_word[i]:
            print(f'correct letter {guess[i]} and position')
        elif guess[i] in game_word:
            print(f'correct letter {guess[i]}')
        else: print(f'wrong letter {guess[i]}')
