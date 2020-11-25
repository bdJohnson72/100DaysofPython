import random



stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
lives = 6
guess = ''
display = []

chosen_word = str(random.choice(word_list))
print(f'the word is {chosen_word}')
for letter in chosen_word:
    display.append('-')

print(display)
game_over = False
stage = 0

while not game_over:
    guess = input('Please guess a letter\n').lower()


    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    if guess not in chosen_word:
        lives -= 1
        print(f'The letter {guess} is not in the word')
        print(f'Lives remaining = {lives}')
        print(stages[lives])
        stage += 1
    if lives == 0:
        game_over = True
        print('You loose')
    if '-' not in display:
        game_over = True
    print(display)
