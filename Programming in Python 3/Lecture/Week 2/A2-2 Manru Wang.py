# Manru Wang
# ITP 115
# Assignment 2 Extra Credit
# 1/26/2018
# Description: Vending Machine
# This program simulates a quidditch match

#Part 1: Harry Potter Vending Machine (accept more than one galleon)

#Set the prices of items
butterbeer=100
quill=200
prophet=300
book=400
python=500

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
print("     e) Python:",python,"knuts")
q1=input(">")
if q1.lower() !="a" and q1.lower() !="b" and q1.lower() !="c" and q1.lower() !="d" and q1.lower() !="e":
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
if q1.lower()=="b":
    item=str("Quill")
    price=quill
elif q1.lower() == "c":
    item= str("The Daily Prophet")
    price=prophet
elif q1.lower() == "d":
    item = str("Book of Spells")
    price=book
elif q1.lower()=="e":
    item=str("Python")
    price=python
else:
    item = str("Butterbeer")
    price = butterbeer

#Display total price
print("You bought a", item, "for",price, "knuts", "(with coupon of", end=" ")
if q2.lower()=="y":
    print("5",end=" ")
    price=price-5
else:
    print("0",end=" ")
    price=price
print("knuts) and paid with:")

#Enter total payment
print("Galleon:",end="")
payment1=int(input(""))
print("Sickles:",end="")
payment2=int(input(""))
print("Knuts:",end="")
payment3=int(input(""))

#Verify valid payment
while (galleon*payment1+sickle*payment2+knut*payment3-price)<0:
    print("You have entered an invalid value. Please try again.")
    print("You bought a", item, "for", price, "knuts", "(with coupon of", end=" ")
    if q2.lower() == "y":
        print("5", end=" ")
        price=price-5
    else:
        print("0", end=" ")
        price=price
    print("knuts) and paid with:")
    print("Galleon:", end="")
    payment1 = int(input(""))
    print("Sickles:", end="")
    payment2 = int(input(""))
    print("Knuts:", end="")
    payment3 = int(input(""))
    # Otherwise go on with the calculations

#Display the change
print("Here is your change (",end="")
print(galleon*payment1+sickle*payment2+knut*payment3-price,"knuts):")
print("Galleon:",(galleon*payment1+sickle*payment2+knut*payment3-price)//galleon)
print("Sickles:",(galleon*payment1+sickle*payment2+knut*payment3-price)%galleon//sickle)
print("Knuts:",(galleon*payment1+sickle*payment2+knut*payment3-price)%galleon%sickle)

