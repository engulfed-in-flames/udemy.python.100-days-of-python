import turtle as t

def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)
    
def set_heading_counter_clockwise():
    turtle.left(10)
    
def set_heading_clockwise():
    turtle.right(10)
    
def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()
    
if __name__ == "__main__":
    turtle = t.Turtle()
    turtle.speed(20)

    screen = t.Screen()
    screen.setup(width=1280, height=720)

    screen.onkey(fun=move_forwards, key="w")
    screen.onkey(fun=move_backwards, key="s")
    screen.onkey(fun=set_heading_counter_clockwise, key="a")
    screen.onkey(fun=set_heading_clockwise, key="d")
    screen.onkey(fun=clear, key="c")

    screen.listen()
    screen.exitonclick()