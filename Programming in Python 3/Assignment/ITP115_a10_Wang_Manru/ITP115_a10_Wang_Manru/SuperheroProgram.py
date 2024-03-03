
from Superhero import Superhero

def main():
    while True:
        name1=input("Enter fighter #1's name:")
        type1=input("Is fighter #1 a hero or a villain?:")
        attack1=int(input("Enter fighter #1's attack points:"))

        name2 = input("Enter fighter #2's name:")
        type2 = input("Is fighter #2 a hero or a villain?:")
        attack2 = int(input("Enter fighter #2's attack points:"))

        player1=Superhero(name1,type1,attack1)
        player2 = Superhero(name2, type2, attack2)

        print("FIGHTERS")

        print(player1)
        print(player2)

        print("\nBEGINNING BATTLE!\n")
        roundnum = 1
        while player1.isDead() is False and player2.isDead() is False:

            print("======Round",roundnum,"======")
            player1.loseHealth(player2.getAttack())
            player2.loseHealth(player1.getAttack())
            print(player1)
            print(player2)
            roundnum += 1

        if player1.isDead() is True and player2.isDead()is False:
            print(player2.getName()+" won!")

        elif player2.isDead() is True and player1.isDead()is False:
            print(player1.getName()+" won!")

        elif player1.isDead() is True and player2.isDead() is True:
            print("Tie!")

        again=input("Would you like to play again? (y/n) ")
        if again=="y":
            continue
        elif again=="n":
            print("Goodbye!")
            break

main()



