#!/usr/bin/env python
import math
from my_booster import factorial
from time import time
# Find n!
n = 133742

##
#	Run GMP implementation
##
print '======= my_booster ======='
start = time()
res = int(factorial(n)) # Convert to int since math.factorial does that
stop = time()
my_res = str(res)
my_time = stop-start

print 'It took {:f} seconds to find factorial({:d})'.format(my_time, n)
print 'Length of output in base 10: {:d}\n'.format(len(my_res))

##
#	Run Python's math implementaion
##
print '======= math.factorial ======='
start = time()
res = math.factorial(n)
stop = time()
math_res = str(res)
math_time = stop-start

print 'It took {:f} seconds to find factorial({:d})'.format(math_time, n)
print 'Length of output in base 10: {:d}\n'.format(len(math_res))

##
#	Test for equality
##
print '======= equality? ======='
print my_res == math_res, "\n"

##
#
##
print '======= speed up ======='
print math_time/my_time, 'times faster'
