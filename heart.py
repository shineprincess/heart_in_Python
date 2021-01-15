import turtle

turtle.pensize(3)
# turtle.speed(1)

#background - color
turtle.color('black')

turtle.begin_fill()

turtle.fillcolor("#e75480")  # pink inside

turtle.left(150)
turtle.forward(180)

# for semicircle = -90,radius
turtle.circle(-90, 180)

# next circle for up
turtle.setheading(60)

# another semi-circle
turtle.circle(-90, 180)

turtle.forward(180)

# finish our draw
turtle.end_fill()

# turtle window appear until we manually close it
turtle.mainloop()
# if dont write thn window will close automatically as pattern created
