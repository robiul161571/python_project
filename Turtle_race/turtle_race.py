from turtle import Turtle, Screen
import random
race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []
for index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(color[index])
    tim.penup()
    tim.goto(x=-230, y=y_position[index])
    all_turtle.append(tim)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230 :
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Y've won. the {winning_color} is winner")
            else:
                print(f"Y've lost. The {winning_color} is winner")

        rand_int = random.randint(1, 10)
        turtle.forward(rand_int)





screen.exitonclick()