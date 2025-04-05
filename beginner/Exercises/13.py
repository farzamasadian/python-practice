string='hello. my name is farzam asadian. happy to meet you.'
counter = dict()
for letter in string:
    counter[letter] = counter.get(letter,0)+1
{print(f'{each} appeard {counter[each]} times.') for each in list(counter.keys())}
    # print(f'{each} appeard {counter[each]} times.')
# print(counter)