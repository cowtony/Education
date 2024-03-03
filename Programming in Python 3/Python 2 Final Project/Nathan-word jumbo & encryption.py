import random
listl = ["pneumonoultramicroscopicsilicovolcanoconiosis", "afternoon", "sandwitch", "evolution", "revolution"]
while True:
    a = random.choice(listl)  # a = "afternoon"
    # print (a)

    n = len(a)  # n = 9
    print("this is a ", n, "letters words")
    count = 1

    new = a + a[0]  # new = "afternoona"      (a[0] = "a")
    # new = "ternoona"
    # new = "ternoona" + "f"      (a[1] = "f")
    new = new[2:]
    new = new + a[1]

    print("Here is a jumbled version of the word:", new)  # "ternnonaf"
    guess = input("Please make a guess: ")
    while guess != a:
        guess = input("Please try again: ")
        count = count + 1
    if guess == a:
        print("You got it right! You have tried", count, "Times!")
    continue1 = input("Do you want to play again y/n?")
    if continue1 == "y":
        continue
    if continue1 == "n":
        break