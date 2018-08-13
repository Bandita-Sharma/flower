import turtle

def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)
    
def draw_art():
    window=turtle.Screen()
    window.bgcolor("purple")    

    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("pink")
    brad.speed(12)
    for i in range(1,36):
        draw_square(brad)
        brad.right(10)
    brad.right(100)
    brad.forward(200)


    
    window.exitonclick()

draw_art()
