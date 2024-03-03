# Manru Wang
# ITP 115
# Assignment 4 Extra Credit
# 2/9/2018
# Description: Word Jumbled Extra Credit

import random

#Part 1 – Word Jumble Game

#Input word
wordlist=["python","trojan","brandon","holiday"]
word=random.choice(wordlist)

#Define hint
def hint(word):
    if word==wordlist[0]:
        #python
        return "115"
    elif word==wordlist[1]:
        #trojan
        return "USC"
    elif word==wordlist[2]:
        #brandon
        return "TA"
    elif word==wordlist[3]:
        #holiday
        return "2/19"

list1=list(word)
list2=list1[:]
print("The jumbled word is",end=" ")

length1=len(word)

#Jumble the word
while length1>0:
    letter=random.choice(list2)
    print(letter,end="")
    list2.remove(letter)
    length1=length1-1
print("")
guess=input("Please enter your guess:")

#Take and count guesses
time=1
while guess!=False:
    if guess!=word:
        print("Try again.")
        guess = input("Please enter your guess:")
        time=time+1
        if time >=3:
            #Hint over 3 tries
            print("Here is a hint:", hint(word))

    elif guess==word:
        print("You got it!")
        if time<3:
            #Score rewards if without using hint
            print("Your score is:",6-time,"out of 5.")
        break
print("It took you",time,"tries.")