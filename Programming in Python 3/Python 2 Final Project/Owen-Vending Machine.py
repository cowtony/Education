#Harry Potter Vending Machine

'''
Units:
1 galleon = 493 knuts
1 sickle = 29 knuts
1 knut = 1 knut
'''

def main():
    pay = int(input("How much money (Knuts) are you carrying on you at the moment? "))
    print("So, you're carring ", end = "")
    conversion(pay)

    print("\nPlease select an item from the vending machine:")
    print("a) ButterBeer ---------- Price:  58 knuts")
    print("b) Quill --------------- Price:  10 knuts")
    print("c) The Daily Prophet --- Price:   7 knuts")
    print("d) The Book Of Spells -- Price: 400 knuts")
    vend = input("enter the letter of what you want: ")
    if vend == "a":
        price = 58
    elif vend == "b":
        price = 10
    elif vend == "c":
        price = 7
    elif vend == "d":
        price = 400

    ig = input("\ndo you want to share on instagram? If you do, you get 5 knuts off your purchase [case sensitive] (y/n) ")
    if ig == 'y':
        price -= 5
        print("Thanks! You get a coupon for 5 knuts off this purchase. Final price is", price, "Knuts")
    else:
        print("Okay, you will pay regular price.")

    print("\nSo, you got change of ", end = "")
    conversion(pay - price)

    
    
def conversion(knuts):
    galleon = knuts // 493
    knuts %= 493

    sickle = knuts // 29
    knuts %= 29

    print(galleon, "Galleon(s) and", sickle, "Sickle(s) and", knuts, "Knuts.")


main()
