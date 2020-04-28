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
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.speed(0)
        
    def go_up(self):
        self.goto(self.screen_x)

levels=[""];

level_1= [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXXXXXXX  XXX  XXXX",
"X  XXXXXXXXXXX  XXX    XX",
"X    XXXXXXXX  XXXXX  XXX",
"XX   XXXXXXXX          XX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
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
                
marker=Marker();
level=levels[1];
player=Player();
wall=[];

maze_setup(level);


#turn screen updates oof
wn.tracer(0)
#main game loop
while True:
    wn.update()