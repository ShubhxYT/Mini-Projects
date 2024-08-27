import random

top_range = input("Enter the top range of the number : ")
if top_range.isdigit():
    top_range=int(top_range)
    if top_range <= 0:
        print("Pls type a number larger than 0")
    else :
        random_number = random.randint(0,top_range)
        print(random_number)
    
else :
    print("type a valid number")

guesses = 0

while True : 
    user = input("Type a number : ")
    if user.isdigit():
        user = int(user)  
    else :
        print("type a valid number")
        continue # this will go back to above while statement

    if user == random_number:
        print("You got it")
        break
    elif user > random_number:
        print("you were above the number")
    else :
        print("you were below the number")
    guesses += 1

print("you got it in",guesses,"guesses")
