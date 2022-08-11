import random

palavras = ['Ampulheta','Anzol','Almofariz','Bidê','Botija','Candelabro','Dedaleira','Desfibrilador','Diapasão','Echarpe','Estribo','Fagote','Fantoche','Fórceps','Freezer','Navalha','Jaleco','Modem','Narguilé','Nebulizador','Novelo','Oboé','Oxímetro','Pêndulo','Quepe','Selim','Sintetizador','Spray','Urinol','Vuvuzela','Webcam','Xadrez','Xequerê','Xilofone','Zíper']

palavra = random.choice(palavras)
display = []
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
=========
''', '''
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
cont = 6
for l in palavra:
    display.append('_')
print('PALAVRA : ', end='')
while True:
    print(f"{'  '.join(display)}")
    guess = input('\nDigite uma letra')
    #for c in range(0, len(palavra)):
    #    display.append('_')
    #    if palavra[c] == guess:
    #        display[c] = guess

    for i, l in enumerate(palavra):
        if guess == l:
            display[i] = guess
    if '_' not in display or guess == palavra:
        print(f'A palavra era {palavra}')
        print('Vc ganhou!!')
        break
    else:
        if guess not in palavra:
            print(f'A palavra não possui a letra {guess}')
            print(stages[cont])
            cont -= 1
        if cont < 0:
            print('GAME OVER')
            break








