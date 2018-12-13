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
round5score = 0

for turn in range(10)

for turn in range(4):
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
    round5score = 0
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
    
    while True: 
        e = wait_for_move()
        if e.direction == DIRECTION_MIDDLE:
            if x == applex and y == appley:
                sense.set_pixel(x, y, G)
                score += 1
                round5score += 1
            elif x == apple2x and y == apple2y:
                sense.set_pixel(x, y, G)
                score += 1
                round5score += 1
            else:
                sense.show_message("Incorrect")
                break;
            sleep(1)
            sense.clear()
            if round5score == 2:
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

for turn in range(8):
    round8score = 0
    applex = randint(0,7)
    appley = randint(0,7)
    apple2x = randint(0,7)
    apple2y = randint(0,7)
    apple3x = randint(0,7)
    apple3y = randint(0,7)
    print (applex, appley)
    print (apple2x, apple2y)
    print (apple3x, apple3y)

    sense.set_pixel(applex, appley, R)
    sense.set_pixel(apple2x, apple2y, R)
    sense.set_pixel(apple3x, apple3y, R)
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
                round8score += 1
            elif x == apple2x and y == apple2y:
                sense.set_pixel(x, y, G)
                score += 1
                round8score += 1
            elif x == apple3x and y == apple3y:
                sense.set_pixel(x, y, G)
                score += 1
                round8score += 1
            else:
                sense.show_message("Incorrect")
                break;
            sleep(1)
            sense.clear()
            if round8score == 3:
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
        
for turn in range(10):
    sense.show_message("You collected: " + str(score) + " apples")

    


