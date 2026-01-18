import turtle as t
import random
score = 0
boxx, boxy = 0, 0
basketx, baskety = 0, -200
line = 3
t.title("catching game")
t.setup(500, 500)


t.penup()
t.tracer(0, 0)
t.hideturtle()
reset = 1
def box():
    t.penup()
    t.goto(boxx - 20, boxy)  
    t.pendown()
    t.begin_fill()
    
    t.setheading(0)
    for _ in range(4):
        t.forward(20)
        t.left(90)
    t.end_fill()
    t.penup()

def left():
    global line, basketx
    if line != 1:
        line -= 1
    if line == 1:
        basketx = -100
    if line == 2:
        basketx = -50
    if line == 3:
        basketx = 0
    if line == 4:
        basketx = 50
    if line == 5:
        basketx = 100
    t.update()

def right():
    global line, basketx
    if line != 5:
        line += 1
    if line == 1:
        basketx = -100
    if line == 2:
        basketx = -50
    if line == 3:
        basketx = 0
    if line == 4:
        basketx = 50
    if line == 5:
        basketx = 100
    t.update()


def boxmovement():
    global boxx, reset, target
    if reset == 1:
        target = random.randint(1, 5)
        #print(target)
        reset = 0
    
    if target == 1:
        boxx = -100
        updatemovement()
    if target == 2:
        boxx = -50
        updatemovement()
    if target == 3:
        boxx = 0
        updatemovement()
    if target == 4:
        boxx = 50
        updatemovement()
    if target == 5:
        boxx = 100
        updatemovement()
        

def updatemovement():
    global boxx, reset, target, boxy, score
    boxy -= 5
    t.goto(boxx, boxy)
    box()
    if boxy == baskety and line == 1 and target == 1:
        boxx = 0
        boxy = 0
        reset = 1
        score += 1
    if boxy == baskety and line == 2 and target == 2:
        boxx = 0
        boxy = 0
        reset = 1
        score += 1
    if boxy == baskety and line == 3 and target == 3:
        boxx = 0
        boxy = 0
        reset = 1
        score += 1
    if boxy == baskety and line == 4 and target == 4:
        boxx = 0
        boxy = 0
        reset = 1
        score += 1
    if boxy == baskety and line == 5 and target == 5:
        boxx = 0
        boxy = 0
        reset = 1
        score += 1
    if boxy < -200:
        score = 0
        boxx = 0
        boxy = 0
        reset = 1
    
def click(x, y):
    if x > 0:
        right()
    elif x < 0:
        left()

def basket():
    t.goto(basketx, baskety)
    t.pendown()
    t.left(90)
    t.forward(10)
    t.left(180)
    t.forward(10)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(10)
    t.right(180)
    t.forward(10)
    t.left(90)
    t.forward(30)
    t.penup()
t.onscreenclick(click)
t.onkey(left, "a")
t.onkey(right, "d")
t.onkey(left, "Left")
t.onkey(right, "Right")
t.listen()
def mainloop():
    t.clear()
    t.update()
    t.penup()
    box()
    basket()
    boxmovement()
    t.goto(0, 0)
    t.write(f"{score}", font=("Arial", 16, "normal"))
    t.ontimer(mainloop, 30)


mainloop()
t.mainloop()
