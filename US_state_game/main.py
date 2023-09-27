from turtle import Turtle, Screen
import pandas as pd
screen = Screen()
screen.tracer(0)
turtle = Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# def get_mouse_click_coor(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
state = Turtle()
text = Turtle()
data = pd.read_csv("50_states.csv")
state_name = str(data.state)
total_score = 0

def update_score():
    global total_score
    total_score += 1
guess_state = []

while len(guess_state) < 50:
    screen.update()
    answer_state = screen.textinput(title=f"Score: {total_score}/50", prompt="What's another state name?").title()

    if answer_state in state_name:
        guess_state.append(answer_state)
        axis = data[data.state == answer_state]
        a = list(zip(axis['x'], axis['y']))
        state.penup()
        state.hideturtle()
        state.goto(a[0])
        state.write(answer_state)
        update_score()



