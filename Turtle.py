import turtle
import time
import random

WIDTH,HEIGHT = 500,500
COLORS = ['red','green','blue','orange','yellow','black','purple','pink','brown','cyan']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("ENter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric. Try Again!")
            continue #will go back up istead of going down

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Try Again!")

def create_turtles(colors):
    spacing_x = WIDTH//(len(colors)+1)
    turtles = []
    for i , color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()

        racer.setpos(-WIDTH//2 + (i+1)*spacing_x , -HEIGHT//2 + 20)

        racer.pendown()
        turtles.append(racer)

    return turtles

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for i,racer in enumerate(turtles):
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos() #give the racer position
            if y >= HEIGHT // 2 -10:
                return colors[i]

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing!')


racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print(f"Winner of the race is the {winner} turtle.")

time.sleep(4)