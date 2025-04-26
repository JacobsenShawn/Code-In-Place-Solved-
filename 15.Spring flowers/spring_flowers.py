"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Karel starts in the bottom left corner of a world with 2 empty flower stems, facing East.
    Karel should bloom both flowers with beepers and end in the bottom right corner of the world facing East.
    """
    plant_flower()
    keep_walking()
    plant_flower()  
    keep_walking()




def plant_flower():
    climb_up()
    turn_left()
    guide_rail()
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    climb_down()
    turn_left()

def keep_walking():
    while front_is_clear():
        move()   

def climb_down():
    while front_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()

def guide_rail():
    while right_is_blocked():
        move()

def climb_up():
    while front_is_clear():
        move()
        
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()