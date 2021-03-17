import pandas
import turtle


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "day25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("day25/50_states.csv")
states_found = []

while len(states_found) < len(states.index):
    answer_state = screen.textinput(title=f"{states_found}/{len(states.index)} States correct", prompt="What's another state?").title()

    value = states[states.state == answer_state]
    if not value.empty:
        state_marker = turtle.Turtle()
        state_marker.penup()
        state_marker.goto(int(value.x), int(value.y))
        state_marker.write(value.state.item())
        state_marker.hideturtle()
        states_found.append(value.state.item())
    
    elif answer_state == "Exit":
        break

file = "day25/states_to_learn.csv"
state_list = states[~states.state.isin(states_found)].state.to_list()

pandas.DataFrame(state_list, columns=["State to learn"]).to_csv(file, index=False)


screen.exitonclick()