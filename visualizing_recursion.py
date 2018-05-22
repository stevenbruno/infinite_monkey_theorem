"""
Overview:  Two different tree visualizations, a spiral and a tree. 
		   The turtle module creates a "turtle" that follows instructions 
		   and draws a line.
Author:    Steven Bruno
Resource:  Miller and Ranum Problem Solving with Data Structures and Algorithms
           using python
"""


import turtle


#Recursive spiral

def drawSpiral(myTurtle, lineLen):
	if lineLen > 0:
		myTurtle.forward(lineLen)
		myTurtle.right(90)
		drawSpiral(myTurtle, lineLen - 5)


#Recursive fractal tree

def tree(branchLen, t):
	if branchLen > 5:
		t.forward(branchLen)
		t.right(20)
		tree(branchLen - 15, t)
		t.left(40)
		tree(branchLen - 15, t)
		t.right(20)
		t.backward(branchLen)


def main(): 
	t = turtle.Turtle()
	myWin = turtle.Screen()
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	t.color("green")
	tree(75, t)
	myWin.exitonclick()

main()