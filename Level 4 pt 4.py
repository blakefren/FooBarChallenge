"""
Undercover underground
======================

As you help the rabbits establish more and more resistance groups to fight against Professor Boolean, you need a way to pass messages back and forth.

Luckily there are abandoned tunnels between the warrens of the rabbits, and you need to find the best way to use them. In some cases, Beta Rabbit wants a high level of interconnectedness, especially when the groups show their loyalty and worthiness. In other scenarios the groups should be less intertwined, in case any are compromised by enemy agents or zombits.

Every warren must be connected to every other warren somehow, and no two warrens should ever have more than one tunnel between them. Your assignment: count the number of ways to connect the resistance warrens.

For example, with 3 warrens (denoted A, B, C) and 2 tunnels, there are three distinct ways to connect them:

A-B-C
A-C-B
C-A-B

With 4 warrens and 6 tunnels, the only way to connect them is to connect each warren to every other warren.

Write a function answer(N, K) which returns the number of ways to connect N distinctly labelled warrens with exactly K tunnels, so that there is a path between any two warrens.

The return value must be a string representation of the total number of ways to do so, in base 10.
N will be at least 2 and at most 20.
K will be at least one less than N and at most (N * (N - 1)) / 2

Test cases
==========

Inputs:
    (int) N = 2
    (int) K = 1
Output:
    (string) "1"

Inputs:
    (int) N = 4
    (int) K = 3
Output:
    (string) "16"
    
https://en.wikipedia.org/wiki/Graph_theory
https://en.wikipedia.org/wiki/Graph_enumeration
-graph with N vertices, K edges, simple, undirected, and labeled
-Formula here gives solution for EVERY K and does not let us pick; will not work w/o being very inefficient
http://math.stackexchange.com/questions/689526/how-many-connected-graphs-over-v-vertices-and-e-edges
-Using "Definitely the last addendum" from top solution
"""



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

def answer(N, K):
  # Simple cases
  if K>(N*(N-1)/2) or K<(N-1):
    return 0
  elif K == (N*(N-1)/2):
    return 1
  elif K == (N-1):
    return N**(N-2)
  else:
    # q(n,k) = binomial_coefficient(n*(n-1)/2,k) - Sum(m=0,n-2,binomial_coefficient(n-1,m)*Sum(p=0,k,binomial_coefficient((n-1-m)*(n-2-m)/2,p)*q(m+1,k-p)))
    return binomial_coefficient(N*(N-1)/2,K) - sum_one(N,K)

@memoized
def sum_one(N,K):
  if K>(N*(N-1)/2) or K<(N-1):
    return 0
  elif K == (N-1):
    return N**(N-2)
  else:
    sum = 0
    for i in range(0,N-1):
      sum += binomial_coefficient(N-1,i)*sum_two(i,N,K)
    return sum

@memoized
def sum_two(i,N,K):
  sum = 0
  for j in range(0,K+1):
    if ((N-1-i)*(N-2-i)/2)<j:
      sum += 0
    else:
      sum += binomial_coefficient((N-1-i)*(N-2-i)/2,j)*sum_one(i+1,K-j)
  return sum

@memoized
def binomial_coefficient(n,k):
  if n<0 or k<0 or n<k:
    return 0
  else:
    return math.factorial(n)/math.factorial(k)/math.factorial(n-k)