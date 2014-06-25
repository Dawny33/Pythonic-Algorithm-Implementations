import turtle

turt = turtle.Turtle()
window = turtle.Screen()

def spiral_rec(turt, line):
	if line > 0:
		turt.forward(line)
		turt.right(45)
		spiral_rec(turt, line - 3)


# spiral_rec(turt, 100)
# window.exitonclick()