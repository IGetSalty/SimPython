import sys
import pandas as pd
import numpy as np
import pygame
import matplotlib as plt
import scipy as sp
import sympy as sy
import pytest
from pygame.locals import *

pygame.init()

# Set up Game window and Surface object
DISPLAYSURF = pygame.display.set_mode((900,600))
pygame.display.set_caption('Hello World')

# Setting up Colours
RED     = (255,0,0)
GREEN   = (0,255,0)
BLUE    = (0,0,255)

# Draw on the surface object

# Circle = Surface, Colour, Position, Radius, and...?
circlePosition = (300,50)
x = circlePosition[0]
y = circlePosition[1]

#pygame.draw.circle(DISPLAYSURF,RED,(circlePositionX,circlePositionY),20,0)

# Rectangle = Surface Colour, (position, width, height)
#pygame.draw.rect(DISPLAYSURF,BLUE,(200,150,100,50))


## TODO ##
# Introduce Time
# Ball Class?
# Projectile motion equations
# reset button
# enter power (=initial velocity)


def updateCirclePosition(X,Y):
    speed = 0.1
    gravity = 0.2

    return X+speed,Y+gravity

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quite
            sys.exit()


    # Update Circle position based on fixed speed and gravity
    x,y = updateCirclePosition(x,y)
    pygame.draw.circle(DISPLAYSURF,RED,(x,y),20,0)

    pygame.display.update()
