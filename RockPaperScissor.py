# Rock Paper Scissor

import random 

print("There will be 5 matches between you and your opponent")
print("You have to enter: \n-'R' for Rock\n-'P' for Paper\n-'S'for Scissor")
print()
print("~ Let's Start ~")

def score(user_score, comp_score):
    print("Your Score: ", user_score)
    print("Opponent Score: ", comp_score)
    if user_score == comp_score:
        print("~ It's a Tie ~")
    elif user_score > comp_score:
        print("~ You Won ~")
    else:
        print("~ You Lost ~")

def game():
    n = 0
    user_score = 0
    comp_score = 0

    while n < 5:
        print()
        comp = random.choice(['R','P','S'])

        user = input("Enter: ").upper()

        if user in ["R","P","S"]:

            print("Opponent: ", comp)

            if comp == user:
                print("It's a Tie")

            elif (comp == "R" and user == "P") or (comp == "P" and user == 'S') or (comp == "S" and user == "R"):
                print(" You Win!")
                user_score += 1

            else:
                print("You Lose!")
                comp_score += 1

            n += 1
        else:
            print("Invalid Input")
            continue

    print()
    score (user_score, comp_score)

game()