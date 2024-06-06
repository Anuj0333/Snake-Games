from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-20,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.aad_segment(position)

    def aad_segment(self,position):
        new_segment=(Turtle("square")) 
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head =self.segments[0]

    def extend(self):
        #aad new segnemt to the snake
        self.aad_segment(self.segments[-1].position())


    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x=self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y) 
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading( ) !=DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading( ) !=UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading( ) !=RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading( ) !=LEFT:
            self.head.setheading(RIGHT)