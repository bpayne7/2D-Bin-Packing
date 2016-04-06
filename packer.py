#!/usr/bin/python3
'''

First Fit Decreasing Height Algorithm
and
Next Fit Decreasing Height Algorithm
''' 
from random import randint
from pprint import pprint
from tkinter import *

import math
import time

class Block:
    def __init__(self, w, h,color, x=None, y=None):
        self.placed=False
        self.w=w
        self.h=h
        self.color = color
        self.x=x
        self.y=y
    
    def __repr__(self):
        return "block({}) : {}x{}, {};{}, placed: {}".format(self.color, self.w, self.h, self.x, self.y, self.placed)
    
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
        w.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill=self.color, outline="black")
        
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
        w.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill="black", outline="red")

blocks = list()
i=0
# create blocks

RC = input("Do you want random blocks? (y/n): ")
algorithm = input("Pick Algorithm, First Fit Decreasing Height Algorithm (ff)\
or Next Fit Decreasing Height Algorithm (nf): ")
#RC = 'n'
if RC == 'n':
    while i < 2 :
        blocks.append(Block(300, 150,"orange"))
        i += 1
    i = 0
    while i < 3 :
        blocks.append(Block(30, 10,"yellow"))
        i += 1
    while i < 5 :
        blocks.append(Block(90, 230,"blue"))
        i += 1
    i = 0
    while i < 7 :
        blocks.append(Block(70, 45,"red"))
        i += 1
    i = 0
    while i < 9 :
        block = Block(115, 166,"green")
       # if i in [0,1,2,3]:
         #  block.flip()
        blocks.append(block)
        i += 1
    i = 0
    while i < 10 :
        blocks.append(Block(20, 20,"purple"))
        i += 1
    i = 0
    while i < 13 :
        blocks.append(Block(100, 50,"deeppink"))
        i += 1
    i = 0
    while i < 15 :
        blocks.append(Block(130, 5,"grey"))
        i += 1
    i = 0
elif RC == 'y':
    randnum2w = randint(5,300) # Get random number for the width of 2 blocks
    randnum2h = randint(5,300) # Get random number for the height of 2 blocks
    while i < 2 :
        blocks.append(Block(randnum2w, randnum2h,"orange"))
        i += 1
    i = 0
    randnum3w = randint(5,200) 
    randnum3h = randint(5,200)
    while i < 3 :
        blocks.append(Block(randnum3w, randnum3h,"yellow"))
        i += 1
    randnum5w = randint(5,200) 
    randnum5h = randint(5,200)
    while i < 5 :
        blocks.append(Block(randnum5w, randnum5h,"blue"))
        i += 1
    i = 0
    randnum7w = randint(5,200) 
    randnum7h = randint(5,200)
    while i < 7 :
        blocks.append(Block(randnum7w, randnum7h,"red"))
        i += 1
    i = 0
    randnum9w = randint(5,200) 
    randnum9h = randint(5,200)
    while i < 9 :
        block = Block(randnum9w, randnum9h,"green")
       # if i in [0,1,2,3]:
         #  block.flip()
        blocks.append(block)
        i += 1
    i = 0
    randnum11w = randint(5,200) 
    randnum11h = randint(5,200)
    while i < 11 :
        blocks.append(Block(randnum11w, randnum11h,"purple"))
        i += 1
    i = 0
    randnum13w = randint(5,100) 
    randnum13h = randint(5,100)
    while i < 13 :
        blocks.append(Block(randnum13w, randnum13h,"deeppink"))
        i += 1
    i = 0
    randnum15w = randint(5,100) 
    randnum15h = randint(5,100)
    while i < 15 :
        blocks.append(Block(randnum15w, randnum15h,"grey"))
        i += 1
    i = 0

def showxy(event):
    xm, ym = event.x, event.y
    str1 = "mouse at x=%d  y=%d" % (xm, ym)
    # show cordinates in title
    master.title(str1)

master = Tk()

nodes = list()
w = Canvas(master, width=1000, height=800) # Size of the window
#w = Canvas(master, width=590, height=360)
#w = Canvas(master, width=360, height=260)
w.configure(background='black')
w.bind("<Motion>", showxy)
w.pack()
# Realistic dimensions :  362, 558
#nodes.append(Node(346, 568))
nodes.append(Node(1000, 800)) # Size of the packing area
#nodes.append(Node(360, 260))
        
ymax = 0

if algorithm == 'nf':
    blocks.sort(key = lambda x: (x.h), reverse=False)
    for block in blocks:
        nodes.sort(key = lambda x: x.y)
        for node in nodes :
            if not block.placed : # Check if the block hasn't been placed yet
                if block.fit(node) : # Check if the block fits
                    if ymax < block.y + block.h:
                        ymax = block.y + block.h
                    #node.draw()
                    block.draw() # Draw the block on the canvas 
                    node_down, node_right = node.split(block)
                    if node_right.w > 0:   
                        nodes.append(node_right)                
                    if node_down.w > block.y:
                        nodes.append(node_down)
                    
    
            w.update()
            time.sleep(.0005)   
      

if algorithm == 'ff':
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
                    if ymax < block.y + block.w:
                        #print(block.y+block.w)
                        ymax = block.y + block.w
                    if score1 > score2 or score1 == score2:
                        block.flip()
                    #node.draw() 
                    block.draw() # Draw the block on the canvas
                    
                    node_down, node_right = node.split(block)
                    
                    if node_down.w > 0 and node_down.h > 0:
                        nodes.append(node_down)
                    if node_right.w > 0 and node_right.h > 0:   
                        nodes.append(node_right)
                    #node.draw() 
                else : # If the block still doesn't fit, flip it again
                    block.flip()
            w.update()
            time.sleep(.001)      

pprint(nodes)
pprint(blocks)
print("Bin Height: " + str(ymax))
w.create_rectangle(1500,ymax, 1, ymax+5, fill="white", outline="black")
w.create_text(500, ymax+25,fill = "white", font=("Helvetica", 25), text="BIN HEIGHT: " + str(ymax))
mainloop()
