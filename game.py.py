import random
win_points=int(input("How many points to win: "))
win_points-=1
user_score=0
computer_score=0
while user_score<=win_points and computer_score<=win_points:
    print("1. Stone")
    print("2. Paper")
    print("3. Scissor")
    user_choice=int(input("Make your choice: "))
    computer_choice=random.randint(1, 3)
    choices=("Stone", "Paper", "Scissor")
    print("You chose:", choices[user_choice-1])
    print("Computer chose:", choices[computer_choice-1])
    if user_choice==1:
        if computer_choice==1:
            print("It's a tie")
        elif computer_choice==2:
            print("Computer Scores!!")
            computer_score+=1
        else:
            print("You Score!!")
            user_score+=1
    elif user_choice==2:
        if computer_choice==2:
            print("It's a tie")
        elif computer_choice==3:
            print("Computer Scores!!")
            computer_score+=1
        else:
            print("You Score!!")
            user_score+=1
    elif user_choice==3:
        if computer_choice==3:
            print("It's a tie")
        elif computer_choice==1:
            print("Computer Scores!!")
            computer_score+=1
        else:
            print("You Score!!")
            user_score+=1
    else:
        print("Invalid Choice")
    print("Computer Score: ", computer_score)
    print("User Score: ", user_score)
if user_score==win_points+1:
    print("Congratulations. You Won. Yayyy!!")
elif computer_choice==win_points+1:
    print("Aww, you lost. Better luck next time")

    
