"""
Minion's bored game
===================

There you have it. Yet another pointless "bored" game created by the bored minions of Professor Boolean.

The game is a single player game, played on a board with n squares in a horizontal row. The minion places a token on the left-most square and rolls a special three-sided die.

If the die rolls a "Left", the minion moves the token to a square one space to the left of where it is currently. If there is no square to the left, the game is invalid, and you start again.

If the die rolls a "Stay", the token stays where it is.

If the die rolls a "Right", the minion moves the token to a square, one space to the right of where it is currently. If there is no square to the right, the game is invalid and you start again.

The aim is to roll the dice exactly t times, and be at the rightmost square on the last roll. If you land on the rightmost square before t rolls are done then the only valid dice roll is to roll a "Stay". If you roll anything else, the game is invalid (i.e., you cannot move left or right from the rightmost square).

To make it more interesting, the minions have leaderboards (one for each n,t pair) where each minion submits the game he just played: the sequence of dice rolls. If some minion has already submitted the exact same sequence, they cannot submit a new entry, so the entries in the leader-board correspond to unique games playable.

Since the minions refresh the leaderboards frequently on their mobile devices, as an infiltrating hacker, you are interested in knowing the maximum possible size a leaderboard can have.

Write a function answer(t, n), which given the number of dice rolls t, and the number of squares in the board n, returns the possible number of unique games modulo 123454321. i.e. if the total number is S, then return the remainder upon dividing S by 123454321, the remainder should be an integer between 0 and 123454320 (inclusive).

n and t will be positive integers, no more than 1000. n will be at least 2.

Test cases
==========

Inputs:
    (int) t = 1
    (int) n = 2
Output:
    (int) 1

Inputs:
    (int) t = 3
    (int) n = 2
Output:
    (int) 3
"""



# Define memoized class to store result of each call of recursive method along with parameters
import collections, functools, math, sys
sys.setrecursionlimit(5000) # Foobar maximum

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

def answer(t,n):
  # Not enough rolls for spaces
  if t<(n-1):
    return 0
  # Exactly enough rolls to get to end
  if t==n:
  	return 1
  	
  @memoized
  def move(rolls_left,position):
    if position == (n-1):
      # If at final space, can only roll "stay"
      return 1
    elif rolls_left < (n-position-1) or rolls_left < 0 or position < 0:
      # Not enough rolls for remaining spaces, invalid
      return 0
    elif position == 0:
      # If at first space, can only roll "stay" or "right"
      a = move(rolls_left-1,position) + move(rolls_left-1,position+1)
      return a % 123454321
    else:
      # A space in the middle, with enough remaining rolls
      a = move(rolls_left-1,position+1) + move(rolls_left-1,position) + move(rolls_left-1,position-1)
      return a % 123454321
        
  return move(t,0) % 123454321