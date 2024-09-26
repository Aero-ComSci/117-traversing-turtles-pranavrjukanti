import turtle as trtl


turtle_colors = ["yellow", "purple", "orange", "green", "blue", "red"]
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

vx = 0
we = 0
p = 0

start_positions = [(-250, 0), (-187, 0), (-139, -41), (-129, -100), (-160, -151), (-216, -170)]


class Shapes:
    def __init__(self, vx, we, start_pos):
        self.turtle_color = turtle_colors[vx]
        self.turtle_shape = turtle_shapes[we]
        self.turtle = trtl.Turtle()
        self.turtle.penup()  
        self.turtle.goto(start_pos) 
        self.turtle.pendown()
    
    def display(self):
        self.turtle.color(self.turtle_color)
        self.turtle.shape(self.turtle_shape)
        self.turtle.right(p)
        self.turtle.forward(60)

for i in range(6):
    shape = Shapes(i, i, start_positions[i])
    shape.display()
    p +=40


wn = trtl.Screen()
wn.mainloop()
