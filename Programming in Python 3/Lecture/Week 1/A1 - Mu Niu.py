animal = input("Enter an animal (plural): ")
adjectiveA = input("Enter an adjective: ")
adjectiveB = input("Enter another adjective: ")
verb = input("Enter a verb: ")
verbIng = input("Enter a verb ending in 'ing': ")
numberA = int(input("Enter a number: "))
numberB = int(input("Enter a second number: "))
numberC_str = input("Enter a third number: ")
decimal_str = input("Enter a number with a decimal: ")

print("Today I adopted \"" + str(numberA) + "\" pet \"" + animal + "\".", end = " ")
print("I learned that each animal needs \"" + decimal_str + "\" hours of \"" + verbIng + "\" every day,", end = " ")
print("and that they travel in groups of \"" + numberC_str + "\".", end = " ")
print("They are so \"" + adjectiveA + "\" that I decided to adopt \"" + str(numberB) + "\" more.", end = " ")
print("Now I have \"" + str(numberA + numberB) + "\" \"" + animal + "\" and I am so \"" + adjectiveB + "\" that I want to \"" + verb + "\".")






