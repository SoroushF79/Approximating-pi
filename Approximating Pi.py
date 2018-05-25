"""
Created by Soroush Famili on May 25th, 2018.

This program approximates pi by randomly choosing points in a square. The ratio of the number of points that fall in a inscribed circle 
to the total number of points should tend towards pi/4 as the number of points chosen becomes sufficiently large.
The program utilizes pygame for visual purposes but is probably not the best library to use. The file Thrown.py contains the random function
which is essential to the program.

"""






import pygame
import Thrown
import math, sys, time

pygame.init()
r = 250
width = 500
height = 500
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Approximating pi")

print("This program tries to approximate pi by randomly picking points on the screen.")
print("The ratio of the number of points within the circle to the number of points outside the circle but on the screen should tend towards pi/4 as the number of points increases.")

def circle(surface, color, pos, rad):
    pygame.draw.circle(surface, color, pos, rad)
    
screen.fill(white)

circle(screen, black, (r, r), r)       
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    n = int(input("How many points do you want to test?"))
    total = n
    listt = Thrown.Thrown(n*2)
    i = 0
    circlecount = 0
    while i < n*2:
        circle(screen, red, (listt[i], listt[i + 1]), 2)
        if((math.sqrt(((listt[i] - r)**2) + ((listt[i + 1] - r))**2)) <= r):
            circlecount += 1
        i = i + 2
        pygame.display.update()
    
    ratio = circlecount/total
    app = ratio*4
    print("The ratio of the number of points that landed in the circle to the total number of points is %f." % (ratio))
    print("The ratio multiplied by 4 is your approximation of pi which is %f." % (app))
    p = print("\nThanks for using this program.")
    time.sleep(10)
    sys.exit()



    