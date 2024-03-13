import turtle

s = turtle.Screen()

t = turtle.Turtle() 
t.speed(3)
for i in range(4):
    t.forward(100)
    t.left(90)  

s.mainloop()

