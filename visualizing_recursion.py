"""
Overview:  Two different tree visualizations, a spiral and a tree. 
		   The turtle module creates a "turtle" that follows instructions 
		   and draws a line.
Author:    Steven Bruno
Resource:  Miller and Ranum Problem Solving with Data Structures and Algorithms
           using python
"""


import turtle
from random import randrange as rnd

#Recursive spiral

def drawSpiral(myTurtle, lineLen):
	if lineLen > 0:
		myTurtle.forward(lineLen)
		myTurtle.right(90)
		drawSpiral(myTurtle, lineLen - 5)


#Recursive fractal tree

def tree(branchLen, t):
	if branchLen > 5:
		turn_rad = rnd(15, 45)
		t.color(rnd(0,255), rnd(0,255), rnd(0,255))
		if branchLen <= 15:
			t.color(rnd(0,255), rnd(0,255), rnd(0,255))
		t.pensize(branchLen*0.2)
		t.forward(branchLen)
		t.right(turn_rad)
		tree(branchLen - 15, t)
		t.left(turn_rad * 2)
		tree(branchLen - 15, t)
		t.right(turn_rad)
		t.up()
		t.backward(branchLen)
		t.down()


def main(): 
	t = turtle.Turtle()
	myWin = turtle.Screen()
	myWin.colormode(255)
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	tree(100, t)
	myWin.exitonclick()

main()