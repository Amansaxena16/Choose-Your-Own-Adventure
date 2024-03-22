name = input("Enter your name!! ")
print("Welcome",name,"to this adventure!!")

answer = input("You are on a dirty road and it has come to an end and you can go left or right... Choose left or right!! ").lower()

if(answer == "left"):
    answer = input("You Come to a river, you can walk around it or swim acrooss (Walk/Swim) " ).lower()

    if(answer == "walk"):
        print("You walked for many miles and run out of water and you lost the game!!")

    elif(answer == "swim"):
        print("You swam and were eaten by the eligator and you lost the game!! ");

    else:
        print("Not a valid option. You lose!")

elif(answer == "right"):
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back) ?").lower()

    if(answer == "back"):
        print("You go back and lose!!")
    elif(answer == "cross"):
        answer = input("You cross the bridge and meet a stranger, Do you want to Talk(Yes/No) ").lower()

        if(answer == "yes"):
            print("You Talk to a stranger and they give you a Gold, You Won the Game!!")

        elif(answer == "no"):
            print("You ignored the stranger and they are offended and You Lose the Game!!")

        else:
            print("Wrong Input, You Lose the Game!!")
    
    else:
        print("Wrong Input, You Lose the Game!!")

else:
    print("Wrong input, You Lose the Game!! ")   


print("Thank You for Trying,",name)