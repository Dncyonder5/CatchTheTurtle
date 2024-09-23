import turtle
import random
score = 0
screen = turtle.Screen()
FONT = ('Arial',15,'normal')
grid_size = 10
#score_turtle
coordinate = [-20,-10,0,10,20]
score_turtle = turtle.Turtle()
game_over = False
turtle_list = []
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    screen.bgcolor("light blue")
    screen.title("Catch The Turtle")
    score_turtle.penup()
    top_height = screen.window_height() / 2
    y  = top_height * 0.9
    score_turtle.goto(0,y)
    score_turtle.write(arg="Score: 0" , move=False,align="center",font=(FONT))
def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        global time
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=(FONT))
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * grid_size,y * grid_size)
    turtle_list.append(t)
def setup_turtles():
    for x in coordinate:
        for y in coordinate:
            make_turtle(x,y)
def hide_turtles():
    for t in turtle_list:
        print(turtle_list)
        t.hideturtle()
#recursive function
def show_turtles_randomly():
    hide_turtles()
    if not game_over:
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,500)
#countdown_turtle
countdown_turtle = turtle.Turtle()
def countdown(time):
    global game_over
    countdown_turtle.penup()
    countdown_turtle.hideturtle()
    top_height = screen.window_height() / 2.2
    y = top_height * 0.9
    countdown_turtle.goto(0, y)
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Süre: {time} ", move=False, align="center", font=(FONT))
        screen.ontimer(lambda : countdown(time - 1),1000)

    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=(FONT))
turtle.tracer(0)
setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
countdown(10)
turtle.tracer(1)
turtle.mainloop()
