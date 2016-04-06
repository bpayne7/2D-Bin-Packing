#!/usr/bin/python3
# -*- coding:Utf-8 -*-
from pprint import pprint
from tkinter import *
import math

class Block:
    def __init__(self, w, h, x=None, y=None):
        self.placed=False
        self.w=w
        self.h=h
        self.x=x
        self.y=y
    
    def __repr__(self):
        return "block : {}x{}, {};{}, placed: {}".format(self.w, self.h, self.x, self.y, self.placed)
    
    def fit(self, node):
        if not node.used and node.w >= self.w and node.h >= self.h :
            self.placed = True
            self.x = node.x
            self.y = node.y
            return True
        else:
            return False
    
    def flip(self):
        self.w, self.h = self.h, self.w
    
    def draw(self):
        w.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill="blue", outline="black")
        
    def touching_perimeter(self, max_x, max_y) :
        if self.x+self.w == max_x:
            return self.w+2*self.h
        elif self.y+self.h == max_y:
            return 2*self.w+self.h
        else :
            return self.w+self.h

        
class Node:
    def __init__(self, w, h, x=0, y=0):
        self.used=False
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        
    def __repr__(self):
        return "Node : {}x{}, {};{}, used: {}".format(self.w, self.h, self.x, self.y, self.used)
        
    def find(self, w, h):
        return self.right, self.down
    
    def split(self, block):
        self.used = True
        node_down = Node(self.w, self.h - block.h, self.x, self.y + block.h)
        node_right = Node(self.w - block.w, block.h, self.x + block.w, self.y)
        
        return node_down, node_right
    
    def draw(self):
        w.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill="red", outline="black")

blocks = list()
i=0
while i < 2 :
    blocks.append(Block(90, 230))
    i += 1
i = 0
while i < 10 :
    block = Block(115, 166)
    #if i in [0,1,2,3]:
    #    block.flip()
    blocks.append(block)
    i += 1
i = 0
while i < 0 :
    blocks.append(Block(186, 129))
    i += 1
i = 0
"""i = 0
while i < 9 :
    blocks.append(Block(90, 230))
    i += 1
i = 0
while i < 3 :
    blocks.append(Block(180, 115))
    i += 1"""

def showxy(event):
    xm, ym = event.x, event.y
    str1 = "mouse at x=%d  y=%d" % (xm, ym)
    # show cordinates in title
    master.title(str1)

master = Tk()

nodes = list()
w = Canvas(master, width=346, height=568)
#w = Canvas(master, width=590, height=360)
#w = Canvas(master, width=360, height=260)
w.configure(background='black')
w.bind("<Motion>", showxy)
w.pack()
# Realistic dimensions :  362, 558
nodes.append(Node(346, 568))
#nodes.append(Node(590, 360))
#nodes.append(Node(360, 260))
        
blocks.sort(key = lambda x: (x.h*x.w), reverse=True)

for block in blocks:
    nodes.sort(key = lambda x: x.y)
    for node in nodes :
        if not block.placed : # Check if the block hasn't been placed yet
            if not block.fit(node): # If the block doesn't fit, try to flip it
                block.flip()
            if block.fit(node) : # Check if the block fits
                score1 = block.touching_perimeter(nodes[0].w, nodes[0].h)
                block.flip()
                score2 = block.touching_perimeter(nodes[0].w, nodes[0].h)
                
                if score1 > score2 or score1 == score2 :
                    block.flip()
                
                block.draw() # Draw the block on the canevas
                
                node_down, node_right = node.split(block)
                
                if node_down.w > 0 and node_down.h > 0:
                    nodes.append(node_down)
                if node_right.w > 0 and node_right.h > 0:   
                    nodes.append(node_right)
            else : # If the block still doesn't fit, flip it again
                block.flip()
            #pprint(nodes)
            #input()


pprint(nodes)
pprint(blocks)

mainloop()
