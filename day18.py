from turtle import Turtle, Screen
import random


timmy_the_turtle= Turtle()
# timmy_the_turtle.colormode(255)

# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     random_color= (r,g,b)
#     return random_color
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.backward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.backward(100)

# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)  
#     timmy_the_turtle.pendown()
# colors= ["wheat","SeaGreen","red","yellow","black"]


#drawing different shapes
# def draw_shape(number_sides):
#     angle = 360/  number_sides
#     for _ in range(number_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
        
# for shape_sides in range(3,11):
#     timmy_the_turtle.color(random.choice(colors))
#     draw_shape(shape_sides)        

#working different direction
# direction=[0,90,180,270]
colors=["red","yellow","blue","black","white","green","wheat"]
# timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

# for _ in range(100):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(direction))
    
#drawing circle
def draw_the_spirograph(size_of_gap):
    for _  in range(int(360/ size_of_gap)):
        timmy_the_turtle.color(random.choice(colors))
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading()+ size_of_gap)
draw_the_spirograph(5)


screen= Screen()
screen.exitonclick()