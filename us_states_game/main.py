import turtle
import pandas
from webbrowser import get

screen = turtle.Screen()
screen.title('US States Game')
image = ('blank_states_img.gif')
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_guess = screen.textinput(title=f'{len(guessed_states)}/50', 
                                    prompt='What is another state name?').title()
    if answer_guess != 'Exit':
        if answer_guess in all_states:
            guessed_states.append(answer_guess)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_guess]
            t.goto (int(state_data.x), int(state_data.y))
            t.write(answer_guess)
    else:
        missingstates = []
        for states in all_states:
            if states not in guessed_states:
                missingstates.append(states)   
        new_data = pandas.DataFrame(missingstates)
        new_data.to_csv('statestolearn.csv')
        print(new_data)
        break


screen.exitonclick()
        
