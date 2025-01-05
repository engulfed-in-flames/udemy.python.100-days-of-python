import colorgram as c
import turtle as t
from random import choice


def extract_colors() -> list[tuple[int, int, int]]:
    rgb_colors = []
    
    colors = c.extract("palette.png", 100)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    
    return rgb_colors

if __name__ == "__main__":    
    screen = t.Screen()
    screen.setup(width=1280, height=720)
    screen.colormode(255)
    
    turtle = t.Turtle()
    turtle.speed(20)
    turtle.penup()
    
    colors = extract_colors()
    
    for i in range(10):
        turtle.setheading(225)
        turtle.forward(300)
        turtle.setheading(90)
        turtle.forward(i * 50)
        turtle.setheading(0)
        
        for j in range(10):
            color = choice(colors)
            turtle.dot(20, color)
            turtle.forward(50)
        
        turtle.home()
    
    screen.exitonclick()
    