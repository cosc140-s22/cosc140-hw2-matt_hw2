#######################################################
#
# COSC 140 Homework 2, "face" problem
#
#######################################################

import turtle

t = turtle.Turtle()
s = t.getscreen()
s.title("Self portrait")
s.setworldcoordinates(0, 0, 600, 600)
t.speed('fastest')
s.bgcolor("black")
t.pencolor("grey")
t.pensize(10)

def move_up(degree):
  t.setheading(0)
  t.penup()
  t.left(90)
  t.forward(degree)
  t.right(90)
  t.pendown()

def move_down(degree):
  t.setheading(0)
  t.penup()
  t.right(90)
  t.forward(degree)
  t.left(90)
  t.pendown()

def move_right(degree):
  t.setheading(0)
  t.penup()
  t.forward(degree)
  t.pendown()

def move_left(degree):
  t.setheading(0)
  t.penup()
  t.backward(degree)
  t.pendown()

def eyes(circles, color):
  for i in range(circles):
    if i == 1:
      move_up(circles*2)
      t.dot(circles*1.5)
      move_down(circles*2)
    elif (i < 4):
      t.pencolor(color)
      t.fillcolor(color)
      t.begin_fill()
      t.circle(circles*i)
      t.end_fill()
      t.pencolor("black")
    else:
      t.circle(circles*i)

def make_face(size, color):
  move_right(250)
  t.fillcolor(color)
  t.begin_fill()
  t.circle(size)
  t.end_fill()
  move_left(250)

def make_mouth():
  move_down(100)
  for i in range(2):
    t.forward(300)
    t.right(90)
    t.forward(120)
    t.right(90)
  
  
  
def main():
  make_face(400, "white")
  move_up(400)
  eyes(10, "white")
  move_right(250)
  move_down(100)
  t.circle(50, 180)
  move_down(75)
  move_left(130)
  make_mouth()
  move_up(150)
  move_right(380)
  eyes(10, "blue")
  turtle.done()
    # call the main function for drawing your scene here

#turtle.mainloop()
main()
