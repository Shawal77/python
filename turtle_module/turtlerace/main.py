import turtle
import time
import random

WIDTH,HEIGHT = 500,500
COLORS = [
    'red',
    'green',
    'blue',
    'orange',
    'yellow',
    'black',
    'purple',
    'pink',
    'brown',
    'cyan'
    ]
def init_turtle():
    #create a screen
    #center is 0,0
    #height is what you set it
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Racing!')
def get_no_of_racers():
    racers = 0
    while True:
        racers=input('Enter number of racers(2 to 10): ')
        if racers.isdigit():
            racers=int(racers)
        else:
            print('Input is invalid, not an integer....\n Try again!')
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range 2-10 try again')
def create_turtles(colors):
    turtles=[]
    spacingx=WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacingx,-HEIGHT//2+20)
        turtles.append(racer)
    return turtles
def race(colors):
    turtles=create_turtles(colors)

    while True:
        for racer in turtles:
            distans=random.randrange(1,15)
            racer.pendown()
            racer.forward(distans)

            x,y=racer.pos()
            if y>=(HEIGHT//2)-10:
                return colors[turtles.index(racer)]
def main():
    racers=get_no_of_racers()
    init_turtle()
    random.shuffle(COLORS)
    colors=COLORS[:racers]#list slice
    winner=race(colors)

    print(f'The winner is {winner}')

    time.sleep(5)
if __name__=='__main__':
    main()
