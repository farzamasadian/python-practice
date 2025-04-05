word=input()
word.lower()
new_word=''
for letter in word:
    if letter == 'a' :
        word=word.replace(letter,'')
    if letter == 'e' :
        word=word.replace(letter,'')
    if letter == 'o' :
        word=word.replace(letter,'')
    if letter == 'i' :
        word=word.replace(letter,'')
    if letter == 'u' :
        word=word.replace(letter,'')
for letter in word:
    letter='.'+letter
    new_word+=letter
print(new_word)