from random import choice
import turtle as t


def get_random_rgb() -> tuple:
    r = lambda: choice(range(256))
    return (r(), r(), r())

def draw_spirograph(turtle, radius: int, angle: int) -> None:
    for i in range(360 // angle):
        rgb = get_random_rgb()
        turtle.pencolor(rgb)
        turtle.circle(radius)
        turtle.setheading(turtle.heading() + angle)
        

if __name__ == "__main__":
    screen = t.Screen()
    screen.setup(width=1280, height=720)
    screen.colormode(255)
    
    turtle = t.Turtle()
    turtle.speed(20)
    
    radius = 50
    angle = 10
    
    draw_spirograph(turtle, radius, angle)
    
    screen.exitonclick()