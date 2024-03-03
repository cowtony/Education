import random
firstques = input(print('Hello there! Would you like to translate a word into pig Elvish? (y/n)'))
while firstques != 'y' and firstques != 'n':
    firstques = input(print('Error! Invalid input. Would you like to translate a word into pig Elvish? (y/n)'))
    if firstques != 'y' and firstques !='n':
        continue
    else:
        break
if firstques == 'y':
    secondques = input(print('Enter the word that you want to translate:'))
    secondquesmod = secondques + secondques[0]
    secondquesmod = secondquesmod[1:]
    firstLetter = secondquesmod[0].upper()
    secondquesmod = firstLetter + secondquesmod[1:]
    secondquesmod2 = secondquesmod[:-1] + secondquesmod[-1].lower()
    vowel = ['a', 'e', 'i', 'o', 'u']
    if len(secondques) >= 4:
        secondquesmod2 = secondquesmod2 + vowel[random.randrange(5)]
    else:
        secondquesmod2 = secondquesmod2 + str('en')
    secondquesmod2 = secondquesmod2.replace('k', 'c')
    if secondquesmod2[-1] == 'e':
        secondquesmod2 = secondquesmod2[-1].replace('e','ë')
    print(secondques,'translated to pig Elvish is',secondquesmod2)
elif firstques == 'n':
    print('Thank u come again')