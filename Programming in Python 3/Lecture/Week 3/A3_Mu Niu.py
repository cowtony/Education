import random

while True:
    print("Elcómewó óten heten Igpén Lvísheá ránslátórtë!")
    print("(Welcome to the Pig Elvish translator!)")
    word = input("Please enter a word you would like to translate: ")

    # Take the first letter of the word and move it to the end of the word
    newWord = word + word[0]
    newWord = newWord[1:]

    # If the word is four letters or more, append a random vowel to the end of the word (aeiou)
    vowel = ['a', 'e', 'i', 'o', 'u']
    if len(word) >= 4:
        newWord = newWord + vowel[random.randrange(5)]
    elif len(word) <= 3: #If the word is three letters or fewer, append “en” to the end of the word
        newWord = newWord + "en"

    # Change all k’s to c’s
        newWord = newWord.replace('k', 'c')

    # If there is an e at the end of the word, replace it with ë (e with an umlaut)
    if newWord[-1] == 'e':
        newWord = newWord[0:-1] + 'ë'

    print("'" + word + "' in elvish is:", newWord)
    answer = input("Would you like to translate another word? (y/n): ")
    if answer != 'y':
        break