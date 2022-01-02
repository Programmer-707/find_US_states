import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
dict = data.to_dict()
print(dict)
states = data.state.to_list()
counter = 0
found_states = []
missed_states = []

while len(found_states) < 50:
    answer = screen.textinput(title=f"{counter}/50 Correct States ", prompt="What is the another state's name?").title()

    if answer == "Exit":
        missed_states = [stat for stat in states if stat not in found_states]
        print(missed_states)
        break

    if answer in states and answer not in found_states:
        found_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        counter += 1

        answer_state = data[data.state == answer]

        t.goto(int(answer_state.x), int(answer_state.y))
        t.write(answer_state.state.item())  #or we can use answer easily :)

missed_df = pandas.DataFrame(missed_states)
missed_df.to_csv("Missed_Satates.csv")