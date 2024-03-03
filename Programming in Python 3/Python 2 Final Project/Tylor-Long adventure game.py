x = 1
while True:
    print("")
    print("You are walking down a street and you see a poster of a mountain")
    print("you decided you wanted to climb mountains")
    print("a) climb a rock")
    print("b) climb an actual mountain")
    MountainClimbing = input("What do you do, a or b? ")
    if MountainClimbing == "a":
        print("")
        print("You tripped on the rock and suffered a death by breaking your skull")
        print("THE END")
        MountainClimbingFail = input("Do you want to play again for a better ending, yes or no? ")
        if MountainClimbingFail != "no":
            x = x+1
            continue
        elif MountainClimbingFail == "no":
            break
    elif MountainClimbing == "b":
        print("")
        print("Thanks to your climbing skills")
        print("you conquered a mountain that was one of the tallest in the U.S")
        print("After the mountain, you decided to climb more and more mountains")
        print("You climbed so many mountains")
        print("including Mount Kilimanjaro, Denali, etc")
        print("Except for one, Mount Everest, with all your courage you decided to climb it")
        print("When you got to base camp at Everest, you took a deep breath")
        print("this was going to be a long journey")
        print("a) go right of the mountain and not trust the map you have")
        print("b) go left of the mountain and trust the map")
        EverestBaseCamp = input("What do you do, a or b? ")
        if EverestBaseCamp == "b":
            print("")
            print("You decided to go the way that was shown on the map")
            print("There was a crevice in the mountain")
            print("you tried to avoid it but you got sucked in and fell to your death")
            print("THE END")
            EverestBaseCampFail = input("Do you want to play again for a better ending, yes or no? ")
            if EverestBaseCampFail != "no":
                x = x+1
                continue
            elif EverestBaseCampFail == "no":
                break
        elif EverestBaseCamp == "a":
            print("")
            print("You decided to go on another route and then go to a camp")
            print("You finally got to camp 1, since it was almost 12pm, you decided to go on")
            print("a) go the way it says on the map")
            print("b) go another way again")
            EverestCamp1 = input("What do you do, a or b? ")
            if EverestCamp1 == "b":
                print("")
                print("You decided not to trust the map again") 
                print("A big boulder crashed onto you and crushed you")
                print("THE END")
                EverestCamp1Fail = input("Do you want to play again for a better ending, yes or no? ")
                if EverestCamp1Fail != "no":
                    x = x+1
                    continue
                elif EverestCamp1Fail == "no":
                    break
            elif EverestCamp1 == "a":
                print("")
                print("You finally decided to trust the map")
                print("The map helped you through your journey")
                print("you got to camp 2 faster then you did when you went from base camp to camp 1")
                print("It is now 5pm")
                print("a) go to camp 3")
                print("b) stay at camp 2")
                EverestCamp2 = input("What do you do, a or b? ")
                if EverestCamp2 == "a":
                    print("")
                    print("There was a big snowstorm and a big wind")
                    print("The wind caught you and pulled you away")
                    print("The cold also caught you so you fell and you froze to a terrible death")
                    print("THE END")
                    print("Note: 2nd Worst Ending")
                    EverestCamp2Fail = input("Do you want to play again for a better ending, yes or no? ")
                    if EverestCamp2Fail != "no":
                        x = x+1
                        continue
                    elif EverestCamp2Fail == "no":
                        break
                elif EverestCamp2 == "b":
                    print("")
                    print("You decided to stay")
                    print("There was a big snowstorm and a big wind")
                    print("You were thankful you stayed at camp 2")
                    print("You got up in the morning and you were ready to go")
                    print("a) do what the map says")
                    print("b) don't trust the map")
                    EverestCamp22 = input("What do you do, a or b? ")
                    if EverestCamp22 == "b":
                        print("")
                        print("You decided to not trust the map")
                        print("There was a big crevice and you fell to your death")
                        print("THE END")
                        EverestCamp22Fail = input("Do you want to play again for a better ending, yes or no? ")
                        if EverestCamp22Fail != "no":
                            x = x+1
                            continue
                        elif EverestCamp22Fail == "no":
                            break
                    elif EverestCamp22 == "a":
                        print("")
                        print("At this altitude, you would want to trust the map from now on")
                        print("You put on your oxygen mask")
                        print("There was a little crevice and you stepped back from it just in time")
                        print("a) use a rope to get across")
                        print("b) jump")
                        EverestCrevice = input("What do you do, a or b? ")
                        if EverestCrevice == "a":
                            print("")
                            print("You used your trusty rope")
                            print("You fell from the rope because you didn't have balance")
                            print("THE END")
                            EverestCreviceFail = input("Do you want to play again for a better ending, yes or no? ")
                            if EverestCreviceFail != "no":
                                x = x+1
                                continue
                            elif EverestCreviceFail == "no":
                                break
                        elif EverestCrevice == "b":
                            print("")
                            print("Since it was very little you decided to jump")
                            print("You made the jump just barely")
                            print("You made it to camp 3")
                            print("You decided to go to camp 4 because it was only 1pm")
                            print("There was a big snowstorm, you could barely see")
                            print("a) go left")
                            print("b) go right")
                            EverestCamp3 = input("What do you do, a or b? ")
                            if EverestCamp3 == "a":
                                print("")
                                print("You struggled to find camp 4 in the storm")
                                print("You could never find camp 4")
                                print("You died of dehydration and coldness")
                                print("THE END")
                                EverestCamp3Fail = input("Do you want to play again for a better ending, yes or no? ")
                                if EverestCamp3Fail != "no":
                                    x = x+1
                                    continue
                                elif EverestCamp3Fail == "no":
                                    break
                            elif EverestCamp3 == "b":
                                print("")
                                print("You struggled to find camp 4 in the storm")
                                print("You finally found camp 4 at 8pm")
                                print("You stayed at camp 4")
                                print("In the morning you got up and were ready for the summit")
                                print("During the trip, you had to use a rope")
                                print("To get to the top of a vertical wall")
                                print("a) go right")
                                print("b) go left")
                                EverestCamp4 = input("What do you do, a or b? ")
                                if EverestCamp4 == "b":
                                    print("")
                                    print("You decided to go left of the wall")
                                    print("Nearing the top, you somehow lost grip of the rope")
                                    print("You fell and died")
                                    print("THE END")
                                    EverestCamp4Fail = input("Do you want to play again for a better ending, yes or no? ")
                                    if EverestCamp4Fail != "no":
                                        x = x+1
                                        continue
                                    elif EverestCamp4Fail == "no":
                                        break
                                elif EverestCamp4 == "a":
                                    print("")
                                    print("You decided to go right of the wall")
                                    print("Right is the 'right' way")
                                    print("You finally got to the top of the wall")
                                    print("You were nearing the summit")
                                    print("You were at the very last stage, and most dangerous place to be")
                                    print("You never knew you would do this")
                                    print("But with your courage, you kept going")
                                    print("All this, is an accomplishment that you should be proud of")
                                    print("You saw skeletons")
                                    print("You had a shiver up your spine")
                                    print("The last stage was very hard and dangerous")
                                    print("You had to climb a ladder")
                                    print("You fell from the ladder but it wasn't very high")
                                    print("You kept going")
                                    print("You conquered the ladder")
                                    print("2nd there is a big crevice in the mountain")
                                    print("a) use the rope")
                                    print("b) jump")
                                    EverestBigCrevice = input("What do you do, a or b? ")
                                    if EverestBigCrevice == "b":
                                        print("")
                                        print("You decided to jump")
                                        print("You didn't make the jump")
                                        print("You fell all the way to almost the bottom of Everest")
                                        print("What a terrible death")
                                        print("THE END")
                                        EverestBigCreviceFail = input("Do you want to play again for a better ending, yes or no? ")
                                        if EverestBigCreviceFail != "no":
                                            x = x+1
                                            continue
                                        elif EverestBigCreviceFail == "no":
                                            break
                                    elif EverestBigCrevice == "a":
                                        print("")
                                        print("You used the rope")
                                        print("You got across the crevice")
                                        print("3rd and final step")
                                        print("A really big vertical wall was ahead of you")
                                        print("But a rockslide became underway")
                                        print("You tried to dodge the rocks")
                                        print("a) go left")
                                        print("b) go right")
                                        EverestRockSlide = input("What do you do a or b? ")
                                        if EverestRockSlide == "b":
                                            print("")
                                            print("You went right")
                                            print("A big boulder hit you and crushed you")
                                            print("THE END")
                                            EverestRockSlideFail = input("Do you want to play again for a better ending, yes or no? ")
                                            if EverestRockSlideFail != "no":
                                                x = x+1
                                                continue
                                            elif EverestRockSlideFail == "no":
                                                break
                                        elif EverestRockSlide == "a":
                                            print("")
                                            print("You went left")
                                            print("You dodged all the rocks")
                                            print("You finally went to the vertical wall")
                                            print("You had your oxygen mask on")
                                            print("Turns out, you barely even noticed you had your oxygen mask on")
                                            print("Since after you left camp 2")
                                            print("a) go left")
                                            print("b) go right")
                                            EverestVerticalWall = input("What do you do, a or b? ")
                                            if EverestVerticalWall == "a":
                                                print("")
                                                print("You went left")
                                                print("Nearing the top")
                                                print("You thought this was the end")
                                                print("But no, you lost grip at the last second")
                                                print("You fell to a terrible death")
                                                print("THE END")
                                                print("Note: Worst Ending")
                                                EverestVerticalWallFail = input("Do you want to play again for a better ending, yes or no? ")
                                                if EverestVerticalWallFail != "no":
                                                    x = x+1
                                                    continue
                                                elif EverestVerticalWallFail == "no":
                                                    break
                                            elif EverestVerticalWall == "b":
                                                print("")
                                                print("You went right")
                                                print("Nearing the top")
                                                print("You thought this was the end")
                                                print("And yes, it was")
                                                print("You got to the top")
                                                print("You made it to the summit")
                                                print("4 days, more then half a week")
                                                print("You made it")
                                                print("You got pictures of yourself")
                                                print("You even picked up snow there to keep")
                                                print("You started to head down")
                                                print("You stayed at camp 4")
                                                print("You told everyone at camp 4, you already made the summit")
                                                print("Everyone was proud of you")
                                                print("In the morning you got up and you started heading down the mountain")
                                                print("You stumbled upon the crevice you did after you left camp 2")
                                                print("a) use the rope")
                                                print("b) jump")
                                                EverestLastObstacle = input("What do you do, a or b? ")
                                                if EverestLastObstacle == "b":
                                                    print("")
                                                    print("You jumped")
                                                    print("You didn't make the jump")
                                                    print("THE END")
                                                    EverestLastObstacleFail = input("Do you want to play again for a better ending, yes or no? ")
                                                    if EverestLastObstacleFail != "no":
                                                        x = x+1
                                                        continue
                                                    elif EverestLastObstacleFail == "no":
                                                        break
                                                elif EverestLastObstacle == "a":
                                                    print("")
                                                    print("You used the rope")
                                                    print("You made it across")
                                                    print("You went all the way down the mountain")
                                                    print("Your family congratulated you")
                                                    print("You were proud of yourself")
                                                    print("THE END")
                                                    print("Note: Good Ending")
                                                    if x == 1:
                                                        print("It took you 1 attempt to get the good ending")
                                                        print("Good job buddy")
                                                        break
                                                    elif x > 1:
                                                        print("It took you",x,"attempts to get the good ending")
                                                        print("Good job buddy")
                                                        break
                                
