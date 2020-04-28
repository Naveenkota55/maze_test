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
        self.shape("circle")
        self.penup()
        self.speed(0)

levels=[""];

level_1= [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X XXXXXXXXXXXX  XXX  XXXX",
"X XXXXXXXXXXXX  XXX    XX",
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
                marker.stamp()
marker=Marker();
level=levels[1];
maze_setup(level);