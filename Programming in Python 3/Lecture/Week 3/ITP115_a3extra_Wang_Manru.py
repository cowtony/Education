# Manru Wang
# ITP 115
# Assignment 3 - Extra Credit
#2/2/2018
# Description: Pig Elvish and Largest Number


#Part 1 – Igpén Lvísheá (Pig Elvish)
import random
print("Elcómewó óten heten Igpén Lvísheá ránslátórtë!")
print("Welcome to the Pig Elvish translator!")
word1=input("Please enter a word you would like to translate:")

while word1!=False:
    # 6. If the first letter of the English word is capitalized, make it lower case when you append it to the end. Then capitalize the new first letter of the Pig Elvish word
    if word1.islower() == False:
        word2 = word1.lower()
        word3 = word2[:]

        # 1. Take the first letter of the word and move it to the end of the word
        word3 = word3[1:] + word3[0]
        word3=word3.capitalize()
    else:
        word3 = word1[:]
        word3 = word3[1:] + word3[0]

    # 2. If the word is four letters or more, append a random vowel to the end of the word (aeiou)
    vowels = "aoeiu"
    if len(word3) >= 4:
        word3 = word3[:] + random.choice(vowels)

    # 3. If the word is three letters or fewer, append “en” to the end of the word
    else:
        word3 = word3[:] + "en"

    # 4. Change all k’s to c’s
    word3 = word3.replace("k", "c")

    # 5. If there is an e at the end of the word, replace it with ë (e with an umlaut)
    if word3[len(word3) - 1] == "e":
        word3 = word3[0:len(word3)-1]
        word3=word3[:]+"ë"

    # 7. Randomly add accents (áéíóú) some vowels
    accentvowels="áéíóú"
    star=random.choice(word3)
    if star =="a":
        word3=word3.replace(star,"á")
    elif star=="e":
        word3=word3.replace(star,"é")
    elif star=="o":
        word3=word3.replace(star,"ó")
    elif star == "i":
        word3 = word3.replace(star, "í")
    elif star == "u":
        word3 = word3.replace(star, "ú")
    print(word1, "in elvish is:", word3)

    repeat=input("Would you like to translate another word? (y/n):")
    if repeat=="y":
        word1=input("Please enter a word you would like to translate:")
    elif repeat=="n":
        print("Oodbyega! Aveha aen icenë ayden!\n(Goodbye! Have a nice day!)")
        break

