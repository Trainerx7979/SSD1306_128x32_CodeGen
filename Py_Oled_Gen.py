# -*- coding: utf-8 -*-
"""
------------I2c Graphics code generator-------------------------------------
Simple generator with click on/off interface to generate                   |\
array data for SSD1306 and similar OLED displays.                          ||
Generated data is compatible with Micropython implementations on any       ||
compatible chip. Needs minor modification for same method on CircuitPython,||
and also can be easily converted to Arduino IDE code if no one else wants  ||
to code that.                                                              ||
-TODO                                                                      ||
Add primitive graphics functions, such as line, circle, rectangle etc...   ||
Maybe a toolbar to select them. And instead of binary function, there will ||
also be a on/off fill color selection.                                     ||
--------                                                                   ||
Considering adding options for Serial output, so the array can be          ||
sent to a Micropython or Arduino board and interpreted in real time.       ||
-----                                                                      ||
                                                                           ||
Created on Sat Sep 18 07:09:15 2021                                        ||
                                                                           ||
@author: Jon Berg                                                          ||
----=======================================================================||
                                                      
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import random
import pygame
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 1400
WINDOW_WIDTH = 500
pixel_magic = []
width = 128
height = 32

def plotit():
    plt.title("pixel_plot")
    pixel_plot = plt.imshow(
        data, cmap='Greens', interpolation='nearest', origin='lower')
  
    plt.colorbar(pixel_plot)
    plt.show(pixel_plot)

# importing modules
  
# creating a dataset
data = np.random.random((128, 32, 1))
  
# data is an 3d array  with 
# 10x12x10=1200 elements.
# reshape this 3d array in 2d
# array for plotting
nrows, ncols = 128, 32
data = data.reshape(ncols, nrows)
for f in range(0, 32):
    for e in range(0, 128):
        data[f, e] = 0
# creating a plot
pixel_plot = plt.figure()

# plotting a plot
pixel_plot.add_axes()
  

plotit()

def main():
    global SCREEN, CLOCK
    gcount = 0
    drawing = 0
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    Selected_Tool = 0
    xp1, xp2, yp1, yp2 = 0, 0, 0, 0

    def invert_pixel(y, x):
        rect = pygame.Rect(x*10, y*10, 10, 10)
        if data[31 - y, x] == 0:
            data[31 - y, x] = 1
            pygame.draw.rect(SCREEN, WHITE, rect, 0)
            #plotit()
        elif data[31 - y, x] == 1:
            data[31 - y, x] = 0
            pygame.draw.rect(SCREEN, BLACK, rect, 0)
            #plotit()

    while True:
        drawGrid()
        for event in pygame.event.get():
            if gcount > 10000:
                gcount = 0
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:             
            # Tool Changes with Space Bar.
                if event.key == pygame.K_PAGEDOWN:
                    convdat = []
                    convdat = str(data)
                    with open("Gen_Code.txt", "w") as variable_file:
                        for i in range(31):
                            for u in range(127):
                                if data[i, u] == 1:
                                    variable_file.write("1,")
                                elif data[i, u] == 0:
                                    variable_file.write("0,")
                    variable_file.close()
                if event.key == pygame.K_SPACE:
                    if Selected_Tool == 0:
                        Selected_Tool = 1
                    elif Selected_Tool == 1:
                        Selected_Tool = 0

            if Selected_Tool == 0:
                if event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN depending on what you want.
                    convposx, convposy = (event.pos)
                    convposx = int(convposx / 10)
                    convposy = int(convposy / 10)                
                    if convposx > 127:
                        convposx = 127
                    if convposy > 31:
                        convposy = 31
                    invert_pixel(convposy, convposx)
            elif Selected_Tool == 1:
                gcount = gcount + 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if drawing < 2:
                        drawing = drawing + 1
                        convposx, convposy = (event.pos)
                        convposx = int(convposx / 10)
                        convposy - int(convposy / 10)
                        if convposx > 127:
                            convposx = 127
                        if convposy > 31:
                            convposy = 31
                        xp1 = convposx
                        yp1 = convposy
                elif event.type == pygame.MOUSEBUTTONUP:
                    convposx, convposy = (event.pos)
                    convposx = int(convposx / 10)
                    convposy = int(convposy / 10)                
                    if convposx > 127:
                        convposx = 127
                    if convposy > 31:
                        convposy = 31
                    xp2 = convposx
                    yp2 = convposy
                #if xp1 < 0:
                #    xp1 = 0
                #if yp1 < 0:
                #    yp1 = 0
                #if xp2 < 0:
                #    xp2 = 0
                #if yp2 < 0:
                #    yp2 = 0
                draw = 1
                while draw > 0:
                    if xp1 < xp2:
                        xp1 = xp1 + 1
                        invert_pixel(yp1, xp1)
                    elif xp1 > xp2:
                        xp1 = xp1 - 1
                        invert_pixel(yp1, xp1)
                    elif xp1 == xp2:
                        if yp1 == yp2:
                            invert_pixel(yp1, xp1)
                            drawing = 0
                            draw = 0
                    if yp1 > yp2:
                        yp1 = yp1 - 1
                        invert_pixel(yp1, xp1)
                    elif yp1 < yp2:
                        yp1 = yp1 + 1
                        invert_pixel(yp1, xp1)
                    elif yp1 == yp2:
                        if xp1 == xp2:
                            invert_pixel(yp1, xp1)
                            drawing = 0
                            draw = 0

        pygame.display.update()


def drawGrid():
    blockSize = 10 #Set the size of the grid block
    for x in range(128):
        for y in range(32):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


main()