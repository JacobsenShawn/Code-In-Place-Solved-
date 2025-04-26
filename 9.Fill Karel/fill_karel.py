from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    pass
    """
    Pseudo code:
    Pre -Karel facing east bottom left 
    Post karel facing east op right 

    1 while there is no wall blocking karel 
        have him move forward , put beeper 
    once at the wall turn around , and come back to start point 
    rotate karel to face north , place a beeper then move up 1 row
    have karel face east and repeat the steps from the first row, 
    have kaerl return and repeat moving up to next row 
    repeat until karel can no longer move right due to no more space
    """
    while front_is_clear():
        put_beeper()
        move_across_row()
        return_home()
        turn_right()
        move_up_a_row()
    final_row()

    
# fn for karel to move to the end of the row        
def final_row():
    if facing_north():
        turn_right()
        while front_is_clear():
            move()

#fn for karel to move up the row 
def move_up_a_row():
    if front_is_clear():
        move()
        turn_right()
        
#fn for karel to move across the row
def move_across_row():
    while front_is_clear():
        move()
        put_beeper()
    turn_around()

# fn for karel to return to starting point 
def return_home():
    while front_is_clear():
        move()
    
# fn for karel to turn right 
def turn_right():
    for i in range(3):
        turn_left()

# fn to turn karel around 
def turn_around():
    turn_left()
    turn_left()



# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()