import random

def show_Rules():
    print("\n---RULES---")
    print("1.Rock beats scissors")
    print("2.Scissors beats paper")
    print("3.Paper beats rock")

def determine_winner(user,computer):
    if user==computer:
        return "tie"
    elif (user=="rock" and computer=="scissors") or \
         (user=="scissors" and computer=="paper") or \
         (user=="paper" and computer == "rock"):
        return "user"
    else:
        return "computer"
    
def main_game():
    choices = ["rock","paper","scissors"]

    while True:
        user_score=0
        computer_score=0
        round_number = 1


        print("\n----Welcome to Rock,Paper,Scissors----")
        print("Type rules to see rules or 'quit' to end")

        while True:
            print(f"----Round{round_number}----")

            print("available choices: rock,paper and scissors")
            user_choice=input("Enter your choice: ").lower()

            if user_choice == "quit":
                print("Thanks for playing.")
                print(f"Final score: you: {user_score} and computer: {computer_score}")
                break 

            elif user_choice=="rule":
                show_Rules()
                continue
            elif user_choice not in choices:
                print("Invalid input.Please enter again")
                continue
            computer_choice=random.choice(choices)
            print(f"Computer choose: {computer_choice}")

            result=determine_winner(user_choice,computer_choice)

            if result == "tie":
                print("Game tied")
            elif result == "user":
                print("You won this round")
                user_score+=1
            elif result == "computer":
                print("You loose.Computer won this round")
                computer_score=computer_score+1

            print(f"Final score: you: {user_score} and computer:{computer_score}")
            round_number=round_number+1

        play_again=input("Would you like t play more(yes/no)")
        if play_again.lower()!="yes":
            break


if __name__=="__main__":
    main_game()
    
        








