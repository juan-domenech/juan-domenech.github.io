"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

# https://gist.github.com/justjkk/407919#file-ack_short-py
import sys, resource
sys.setrecursionlimit(50000)

# # http://stackoverflow.com/questions/27269576/modified-ackermann-function-in-python-segmentation-fault
# resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
# sys.setrecursionlimit(10**8)

def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))


for x in range(0, 10):
	for y in range(0, 5):
		print 'Ackermann (%i,%i) is: %i' % (x, y, ackermann(x, y) )


