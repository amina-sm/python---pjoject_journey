import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C:\\Users\\Emmy\\Desktop\\ASM\\Journey1\\Day25\\day-25-us-states-game-start\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(
    "C:\\Users\\Emmy\\Desktop\\ASM\\Journey1\\Day25\\day-25-us-states-game-start\\50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# how to get coordinate of x and y
# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 states Correct", prompt="What's another state's name").title()
    print(answer_state)
    if answer_state=="Exit":
        
    if answer_state in answer_state:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


screen.exitonclick()
