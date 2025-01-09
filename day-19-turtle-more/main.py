import turtle as t
from random import randint

width = 720
height = 480

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False

if __name__ == "__main__":
    screen = t.Screen()
    screen.setup(width=width, height=height)
    
    user_bet = screen.textinput("Make you bet", "Which turtle will win? Enter a color: ")
    
    if user_bet in colors:
        is_race_on = True
        
    turtles = []
    winning_color = None
    
    
    
    for i in range(6):
        turtle = t.Turtle(shape="turtle")
        turtle.color(colors[i])
        turtle.speed(5)
        turtle.penup()
        
        x = -(width // 2) + 20
        y = -90 + (i + 1) * 30
        
        turtle.goto(x=x, y=y)
        turtles.append(turtle)

        
    while is_race_on:
        for turtle in turtles:
            distance = randint(1, 10)
            turtle.forward(distance)
            
            if turtle.xcor() > (width // 2) - 10:
                winning_color = turtle.pencolor()
                is_race_on = False
                break
        
    if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner!")
    else:
        print(f"You've lost! The {winning_color} turtle is the winner!")
        
    screen.exitonclick()