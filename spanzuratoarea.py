# Reguli:
# Prima si ultima litera se afiseaza
# Daca litera de inceput sau de sfarsit se gaseste in interiorul cuvantului, aceasta se va afisa.
# Jucatorul are nevoie de 7 incercari
word = 'teleenciclopedie'
start_letter = word[0]
end_letter = word[-1]
display_word = ''
for let in word.lower():
    if let != start_letter and let != end_letter:
        let = '_'
    display_word += let
attempts = 7
tried_chars = []
while attempts > 0:
    print(f'Cuvantul este {display_word}. Mai aveti {attempts} incercari.')
    letter = input('Introduceti litera: ').lower()
    if len(letter) != 1:
        print('Va rugam introduceti o singura litera!')
        continue
    elif not letter.isalpha():
        print('Va rugam introduceti doar litere!')
        continue
    if letter in word:
        if letter in tried_chars:
            print(f'Litera {letter} a mai fost folosita. Literele incercate: {tried_chars}.')
        for index, caracter in enumerate(word.lower()):
            if letter == caracter:
                if letter not in tried_chars:
                    tried_chars.append(letter)
                display_word = display_word[:index] + letter + display_word[index+1:]
    else:
        if letter not in tried_chars:
            tried_chars.append(letter)
            attempts -= 1
        else:
            print(f'Litera {letter} a mai fost folosita. Literele incercate: {tried_chars}.')
    if attempts == 0:
        print(f'Ati pierdut! Cuvantul era "{word}".')
    elif display_word == word: # sau elif '_' not in display_word
        print(f'Felicitari! Ai castigat! Cuvantul gasit este: "{display_word}.')
        break
