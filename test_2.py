#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:10:55 2020

@author: naveenkota
"""

import turtle

wn=turtle.Screen();
wn.bgcolor("white");
wn.setup(700,700);
wn.title("Maze 2");

class Marker(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("black")
        self.shape("square")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("red")
        self.shape("square")
        self.penup()
        self.speed(0)
        
    def go_up(self):
        
        move_x= self.xcor()
        move_y= self.ycor()+24
        if (move_x,move_y) not in wall:
            self.goto(move_x,move_y)
        
    
    def go_down(self):
        move_x= self.xcor()
        move_y= self.ycor()-24
        if (move_x,move_y) not in wall:
            self.goto(move_x,move_y)
        
        
    def go_right(self):
        move_x= self.xcor()+24
        move_y= self.ycor()
        if (move_x,move_y) not in wall:
            self.goto(move_x,move_y)
    
    def go_left(self):
        move_x= self.xcor()-24
        move_y= self.ycor()
        if (move_x,move_y) not in wall:
            self.goto(move_x,move_y)

levels=[""];

level_1= [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXXXXXXX  XXX GXXX",
"X  XXXXXXXXXXX  XXX    XX",
"X    XXXXXXXX  XXXXX  XXX",
"XX   XXXXXXXX    G     XX",
"XX   XXXXXXXXXXXX  XXXXXX",
"XX  XXXXXXXXXXXX  XXXXXXX",
"XXX                 XXXXX",
"XXXXXXX   XXX XX  XXXXXXX",
"XXXXXXX   XXXGXX  XXXXXXX",
"XXXX      XXXXXX  XXXXXXX",
"XXXX      XXXXXX  XXXXXXX",
"XXXXXXXXXXXXXXXX  XXXXXXX",
"XXXXX              XXX GX",
"XXXXX    XXXXXXXXXXXXX  X",
"XXXXX    XXXXXXXXXXXX  XX",
"XXXXX                  XX",
"XXXXXXXXX      XXXXXXXXXX",
"XXXXXXXXX      XXXXXXXXXX",
"XXXXXXXXX      XXXXXXXXXX",
"XXXXXXXXX            XXXX",
"XXXXXXXXXXXXXXXXX    XXXX",
"XXXXX               GXXXX",
"XXXXXG  XXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
];
     
levels.append(level_1);



            
def maze_setup(level):
   for y in range(len(level)):
       for x in range(len(level[y])):
            charc=level[y][x];
            screen_x= -288 + (x*24);
            screen_y =288- (y*24);
            
            if charc=="X":
                marker.goto(screen_x,screen_y);
                marker.stamp();
                wall.append((screen_x,screen_y))
               
            if charc=="P":
                player.goto(screen_x,screen_y);
                
            
            if charc=="G":
                player.goto(screen_)
                
marker=Marker();
level=levels[1];
player=Player();
wall=[];

maze_setup(level);

turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")


#turn screen updates oof
wn.tracer(0)
#main game loop
while True:
    wn.update()