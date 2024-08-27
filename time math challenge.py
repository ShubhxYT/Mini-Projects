import random
import time

#can add as money operators as we are using eval func
OPERATORS = ["+","-","*"] 
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEM = 5

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operators = random.choice(OPERATORS) #random from lst

    expr = str(left) +operators+str(right)

    #evaluate as python expression (no need to use if statements for adding or subtracting anything)
    answer = eval(expr)

    # print(expr,"=",answer)
    return expr,answer


wrong = 0
input("Press Enter to Start!")
print("-----------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEM):
    expr,answer = generate_problem()
    while True:
        user = input("Problem # "+ str(i+1) + " : "+ expr + " = ")
        if user == str(answer):
            break
        print("Wrong")
        wrong+=1

end_time = time.time()
total_time = end_time - start_time

print("------------------------------")
print("Nice Work ! You finished in ",round(total_time,1),"seconds")