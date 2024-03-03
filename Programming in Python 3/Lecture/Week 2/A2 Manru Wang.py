# Manru Wang
# ITP 115
# Assignment 2
# 1/26/2018
# Description: Vending Machine and Choose Your Own Adventure Game
# This program simulates a quidditch match

#Part 1: Harry Potter Vending Machine

#Set the prices of items
butterbeer=58
quill=10
prophet=7
book=400

#Set the value of each currency
galleon=493
sickle=29
knut=1

#Select item to purchase
print("Please select an item from the vending machine:")
print("     a) Butterbeer:",butterbeer,"knuts")
print("     b) Quill:",quill,"knuts")
print("     c) The Daily:",prophet,"knuts")
print("     d) Book of Spells:",book,"knuts")
q1=input(">")
if q1.lower() !="a" and q1.lower() !="b" and q1.lower() !="c" and q1.lower() !="d":
    print("You have entered an invalid option. You will be given a Butterbeer for 58 knuts.")

#Ask if share on Instagram to get discount
q2=input("Will you share this on Instagram? (y/n):")
if q2.lower()=="y":
    print("Thanks! You get 5 knuts off your purchase")
elif q2.lower()=="n":
    print("")
else:
    print("You have entered an invalid option. No coupon will be used")
print("")

#Display total price and payment
if q1.lower()=="b":
    item=str("Quill")
    price=quill
elif q1.lower() == "c":
    item= str("The Daily Prophet")
    price=prophet
elif q1.lower() == "d":
    item = str("Book of Spells")
    price=book
else:
    item = str("Butterbeer")
    price = butterbeer
print("You bought a", item, "for", price, "knuts", "(with coupon of", end=" ")
if q2.lower()=="y":
    print("5",end=" ")
    price=price-5
else:
    print("0",end=" ")
print("knuts) and paid with one galleon.")

#Display the change
print("Here is your change (",end="")
print(galleon - price, "knuts):")
print("Sickles:", (galleon - price) // sickle)
print("Knuts:", (galleon - price) % sickle)
print("")
print("")
print("")


#Part 2: Choose Your Own Adventure

#Intro
print("Welcome to a choose your own adventure game.")
print("")
print("It is summertime again, vacation time. You go to your uncle's house. He takes you on a tour around the city. There are many old buildings, but the oldest of all is on Main Street. The address is 880. He says that it is haunted, but you don't believe him.")
print("")

#Question 1
print("Do you:")
print("a) Go inside the house")
print("b) Stay there")
print("c) Continue walking")
q3=input(">")
print("")
if q3.lower() !="a" and q3.lower() !="b" and q3.lower() !="c":
    print("You have entered an invalid option. You will stay there.")
print("")

#Option 1
if q3.lower()=="a":
    print("You say, \"I will go inside.\" He says, \"I want to watch you.\" You start up the stone steps of the old haunted house. You open the door and step inside and suddenly a sharp arrow streaks across in front of you! But it misses you.")
    print("")
    print("a) Go up the staircase")
    print("b) Go through the swinging doors")
    q4=input(">")
    print("")
    if q4.lower() != "a" and q4.lower() != "b":
        print("You have entered an invalid option. You will go up the staircase.")
    print("")

    #Option 1.1
    if q4.lower()=="b":
        print("You go through the swinging doors. Behind the swinging doors you come across a treasure chest. Congrats! It appears to be full of gold.")

    #Option 1.2
    else:
        print("You go up the staircase. There is only one door. You open it and find a skeleton!!!")
    print("")
    print("THE END")

#Option 2
elif q3.lower()=="c":
    print("You continue walking down the sidewalk when you see a split in the road.")
    print("")
    print("Do you:")
    print("a) Go left.")
    print("b) Go right.")
    q6=input(">")
    print("")
    if q6.lower() != "a" and q6.lower() != "b":
        print("You have entered an invalid option. You will go right.")
    print("")

    #Option 2.1
    if q6.lower()=="a":
        print("You see a laptop. It asks you to finish ITP assignment #843.")

    #Option 2.2
    else:
        print("You find a dollar on the sidewalk. It's your lucky day!")
    print("")
    print("THE END")

#Option 3
else:
    print("You say,\"I will stay here\",You wait for 3 seconds and the floor you are stepping on cracked.")
    print("")
    print("Do you:")
    print("a) Wait and see what will happen")
    print("b) Run away")
    q5=input(">")
    print("")
    if q5.lower() != "a" and q5.lower() != "b":
        print("You have entered an invalid option. You will wait and see what will happen.")
    print("")

    #Option 3.1
    if q5.lower()=="b":
        print("The floor break into pieces and you fall down to the basement where you see 48 ghosts aroundyou.")

    #Option 3.2
    else:
        print("You feel something on your shoulder, and a powerful hand is picking you up to the air.")
        print("")
    print("THE END")

