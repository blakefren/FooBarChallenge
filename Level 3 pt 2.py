# Save Beta Rabbit
# ================

# Oh no! The mad Professor Boolean has trapped Beta Rabbit in an NxN grid of rooms. In the center of each room (except for the top left room) is a hungry zombie. In order to be freed, and to avoid being eaten, Beta Rabbit must move through this grid and feed the zombies.

# Beta Rabbit starts at the top left room of the grid. For each room in the grid, there is a door to the room above, below, left, and right. There is no door in cases where there is no room in that direction. However, the doors are locked in such a way that Beta Rabbit can only ever move to the room below or to the right. Once Beta Rabbit enters a room, the zombie immediately starts crawling towards him, and he must feed the zombie until it is full to ward it off. Thankfully, Beta Rabbit took a class about zombies and knows how many units of food each zombie needs be full.

# To be freed, Beta Rabbit needs to make his way to the bottom right room (which also has a hungry zombie) and have used most of the limited food he has. He decides to take the path through the grid such that he ends up with as little food as possible at the end.

# Write a function answer(food, grid) that returns the number of units of food Beta Rabbit will have at the end, given that he takes a route using up as much food as possible without him being eaten, and ends at the bottom right room. If there does not exist a route in which Beta Rabbit will not be eaten, then return -1.

# food is the amount of food Beta Rabbit starts with, and will be a positive integer no larger than 200.

# grid will be a list of N elements. Each element of grid will itself be a list of N integers each, denoting a single row of N rooms. The first element of grid will be the list denoting the top row, the second element will be the list denoting second row from the top, and so on until the last element, which is the list denoting the bottom row. In the list denoting a single row, the first element will be the amount of food the zombie in the left-most room in that row needs, the second element will be the amount the zombie in the room to its immediate right needs and so on. The top left room will always contain the integer 0, to indicate that there is no zombie there.

# The number of rows N will not exceed 20, and the amount of food each zombie requires will be a positive integer not exceeding 10.

# Test cases
# ==========

# Inputs:
#     (int) food = 7
#     (int) grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
# Output:
#     (int) 0
#     print answer(7,[[0, 2, 5], [1, 1, 3], [2, 1, 1]])

# Inputs:
#     (int) food = 12
#     (int) grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
# Output:
#     (int) 1
#     print answer(12,[[0, 2, 5], [1, 1, 3], [2, 1, 1]])

# These classes are needed for memoizing the recursive call
import collections
import functools

# Define memoized class to store result of each call of test() along with parameters
class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)

# Actual answer method
def answer(food, grid):
    if food<(2*len(grid)-2):
        return -1
        
    @memoized
    def test(food_remaining,grid_x,grid_y):
        # Subtract food, check simple cases
        food_remaining -= grid[grid_y][grid_x]
        if food_remaining==0 and grid_x==len(grid[grid_y])-1 and grid_y==len(grid)-1:
            return 0
        if food_remaining<0:
            return -1
            
        # Check complex cases, return value
        if grid_x==len(grid[grid_y])-1 and grid_y==len(grid)-1:
            return food_remaining
        elif grid_x==len(grid[grid_y])-1:
            return test(food_remaining,grid_x,grid_y+1)
        elif grid_y==len(grid)-1:
            return test(food_remaining,grid_x+1,grid_y)
        else:
            test_a = test(food_remaining,grid_x+1,grid_y)
            test_b = test(food_remaining,grid_x,grid_y+1)
            if test_a == -1 and test_b != -1:
                return test_b
            elif test_a != -1 and test_b == -1:
                return test_a
            elif test_a == -1 and test_b == -1:
                return -1
            else:
                return min(test_a,test_b)
    
    return test(food,0,0)