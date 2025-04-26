"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Places beepers in a zig zag pattern.
    """
    # pre karel facing east 
    # postkarel facing east 

# create a while loop because we dont know how many spaces this will continue 
    while front_is_clear():
        zig_one_zag() # Places a single pair of beepers 
        move_to_next_zigzag_spot() # move to next spot to repeat 

def zig_one_zag(): 
    """

    """
    put_beeper()
    turn_left()
    move()
    turn_right()
    
    if front_is_clear(): # If we remove this check, the code will work, but only on even-column-numbered worlds
        # Only place second beeper if Karel isn't already at the rightmost column of the world
        move()
        put_beeper()

  
# teach to turn right 
def turn_right():
    for i in range(3):
        turn_left()

def move_to_next_zigzag_spot():
    """
    Moves Karel to the next spot to perform zig_one_zag(). Karel starts facing East in row 2, and will end up in row 1.
    If Karel is not facing a wall, Karel will end up one column greater than where Karel started. Otherwise, Karel will be in the same column as initially.
    """
    turn_right()  # Face South
    move()  # Move down to row 1
    turn_left()  # Face East
    if front_is_clear():  # Move to next column if possible
        move()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()