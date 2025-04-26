from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    """
    Pseudo Code:
    Pre- Karel faces East
    create a loop to repeat this action 4 times 

    turn north
    while front is clear (move_up_to_wall)
        place a beeper 
            move 
    turn around 
     while front clear (move_down_to_floor)
        move
    turn left  facing East position

    create a fn to move 4 spaces
    repeat  the above up / down commands


    Post- karel faces East
    """
    for i in range(3):
        full_column()
        for b in range(4):
             move()
    full_column()

    
def full_column():
    turn_left()
    build_up_column()
    scale_down_column()
    turn_left()


def build_up_column():    
    while front_is_clear():
        put_beeper()
        move()
    turn_around()
    put_beeper()

def scale_down_column():
    while front_is_clear():
        move()
    
        
def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()