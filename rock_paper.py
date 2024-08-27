import random

user_wins = 0
computer_wins = 0

while True :
    user_input = input("Type Rock/Paper/Scissors or q to quit : ").lower()
    if user_input == "q":
        break

    lst = ["rock","paper","scissors"]
    if user_input not in lst:
        continue

    random_no = random.randint(0,2)
    bot = lst[random_no]
    print("Computer picked",bot)

    if user_input == "rock" and bot == "scissors":
        print("You won\n")
        user_wins += 1
        continue
    elif user_input == "paper" and bot == "rock":
        print("You won\n")
        user_wins += 1
        continue
    elif user_input == "scissors" and bot == "paper":
        print("You won\n")
        user_wins += 1
        continue
    else:
        print("You Lost !\n")
        computer_wins +=1

print("You Won",user_wins,"times.")
print("computer Won",computer_wins,"times.")       
print("Thanks for Playing")
    

