import random
from sense_hat import *
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

def wait_for_move():
    while True:
        e = sense.stick.wait_for_event()
        if e.action != ACTION_RELEASED:
            return e

R = (255, 0, 0)
Y = (255, 0, 0)
G = (0, 255, 0)
W = (255, 255, 255)

score = 0

for turns in range(4):
    applex = randint(0,7)
    appley = randint(0,7)
    print (applex, appley)

    sense.set_pixel(applex, appley, R)
    sleep(2)
    sense.clear()

    x = randint(0,7)
    y = randint(0,7)
    sense.set_pixel(x, y, W)
    
    while True:
        e = wait_for_move()
        if e.direction == DIRECTION_MIDDLE:
            if x == applex and y == appley:
                sense.set_pixel(x, y, G)
                score += 1
            else:
                sense.show_message("Incorrect")
            sleep(1)
            sense.clear()
            break;
        
        sense.clear()
        if e.direction == DIRECTION_UP and y > 0:
            y = y - 1
        elif e.direction == DIRECTION_DOWN and y < 7:
            y = y + 1
        elif e.direction == DIRECTION_LEFT and x > 0:
            x = x - 1
        elif e.direction == DIRECTION_RIGHT and x < 7:
            x = x + 1
            
        sense.set_pixel(x, y, W)

for turn in range(5):
    applex = randint(0,7)
    appley = randint(0,7)
    apple2x = randint(0,7)
    apple2y = randint(0,7)
    print (applex, appley)
    print (apple2x, apple2y)

    sense.set_pixel(applex, appley, R)
    sense.set_pixel(apple2x, apple2y, R)
    sleep(2)
    sense.clear()

    x = randint(0,7)
    y = randint(0,7)
    sense.set_pixel(x, y, W)
    
    while True: #fix to have one stay if you get it right and you have to look for the next one
        #don't have the level move on if you get one right
        e = wait_for_move()
        if e.direction == DIRECTION_MIDDLE:
            if x == applex and y == appley:
                sense.set_pixel(x, y, G)
                score += 1
            elif x == apple2x and y == apple2y:
                sense.set_pixel(x, y, G)
                score += 1
            else:
                sense.show_message("Incorrect")
            sleep(1)
            sense.clear()
            break;

        sense.clear()
        if e.direction == DIRECTION_UP and y > 0:
            y = y - 1
        elif e.direction == DIRECTION_DOWN and y < 7:
            y = y + 1
        elif e.direction == DIRECTION_LEFT and x > 0:
            x = x - 1
        elif e.direction == DIRECTION_RIGHT and x < 7:
            x = x + 1
            
        sense.set_pixel(x, y, W)
    
sense.show_message("Good job, you collected: " + str(score) + " apples")
    
