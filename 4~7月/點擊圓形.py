import turtle

def circle(x, y):
    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(x, y)
    t.color("red")
    t.down()
    t.speed(2)
    t.circle(10)

s = turtle.Screen()
s.onclick(circle)
s.mainloop()











































