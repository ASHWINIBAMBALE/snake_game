from turtle import Turtle, position
POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_FORWARD=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self) :
        self.snake_body=[]
        self.create_snake()
        self.head=self.snake_body[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_parts(position)
    def add_parts(self,position):
        tim=Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.snake_body.append(tim)
    def extend(self):
        self.add_parts(self.snake_body[-1].position())
    def move(self):
        for seg_num in range(len(self.snake_body)-1,0,-1 ):
            new_x=self.snake_body[seg_num-1].xcor()
            new_y=self.snake_body[seg_num-1].ycor()
            self.snake_body[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_FORWARD)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):     
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):     
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):     
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    
