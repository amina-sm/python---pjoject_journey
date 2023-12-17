# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# creating dots painting
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(254, 254, 253), (15, 17, 40), (240, 251, 251), (95, 223, 223), (15, 15, 14), (85, 85, 83), (252, 218, 0), (253, 224, 58), (246, 0, 0), (177, 159, 158),
              (246, 42, 40), (145, 151, 166), (94, 98, 116), (205, 210, 218), (245, 155, 154), (52, 60, 90), (108, 119, 152), (244, 122, 123), (247, 210, 211), (95, 198, 199)]
tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_dots = 100

for dot_count in range(1, number_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
