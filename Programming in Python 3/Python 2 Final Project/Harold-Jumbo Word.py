import random

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    print("Elcómewó óten heten Igpén Lvísheá ránslátórtë!")
    word = input("Input a word you would like to translate: ")
# Take the first letter of the word and move it to the end of the word
    newWord = word + word[0]   # add the first letter to end
    newWord = newWord[1:]    	# remove the first letter

    if len(word) >= 4:
        newWord = newWord + vowel[random.randrange(5)]
# Replace all k's to c's
    newWord = newWord.replace('K','C')
    print(newWord)
    play = input("would you like to translate another word?y/n")
    if play == 'n':
        print("Have a nice day!")
        break

