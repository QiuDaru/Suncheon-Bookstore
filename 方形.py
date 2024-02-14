import turtle

s = turtle.Screen()

t = turtle.Turtle() 

for i in range(4):
    t.forward(100)
    t.left(90)  # 將左轉角度改為90度

s.mainloop()

