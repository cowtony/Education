# Manru Wang
# ITP 115
# Assignment 4
# 2/9/2018
# Description: Word Jumbled and Encryption

import random

#Part 1 – Word Jumble Game

#Input word
wordlist=["python","trojan","brandon","holiday"]
word=random.choice(wordlist)
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

    elif guess==word:
        print("You got it!")
        break
print("It took you",time,"tries.")



#Part 2 – Encrypt / Decrypt
print("")
msg=input("Enter a message:")
num=int(input("Enter a number to shift by (0-25):"))

index=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list1=list(msg)
list2=list1[:]
decrypt=[]
#Encrypting message
print("Encrypting message....")
print("\tEncrypted message:",end="")
for item in list2:
    if item in index:
        encrypted1=index[(index.index(item) + num)%26]
        decrypt.append(encrypted1)
        print(encrypted1, end="")
    else:
        encrypted2=item
        decrypt.append(encrypted2)
        print(encrypted2,end="")
#Decrypting message
print("")
print("Decrypting message....")
print("\tDecrypted message:",end="")
for item in decrypt:
    print(item,end="")
print("\n\tOriginal message:",end="")
for item in decrypt:
    if item in index:
        decrypted1=index[index.index(item) - num]
        print(decrypted1, end="")
    else:
        decrypted2=item
        print(decrypted2,end="")



