word=input()
if word.count('l')>=2:
    if word.find('h')<word.find('e') and word.find('e') < word.find('l') and word.find('l')<word.find('o'):
        print('yes')
    else:
        print('no')
        