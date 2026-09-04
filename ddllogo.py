#Interactive DDL LOGO WITH PYTHON!

import turtle

t = turtle.Turtle()

#First Letter - D
t.penup()
t.goto(-200, 10)
t.pendown()
t.setheading(90)
t.forward(180)
t.setheading(360)
t.circle(-90, 180)

#Second Letter - D
t.penup()
t.goto(-50, 10)
t.pendown()
t.setheading(90)
t.forward(180)
t.setheading(360)
t.circle(-90, 180)

#Third Letter - L
t.penup()
t.goto(100, 190)       
t.pendown()
t.setheading(270)   
t.forward(180)      
t.setheading(0)     
t.forward(90)   

#Draw
turtle.done()