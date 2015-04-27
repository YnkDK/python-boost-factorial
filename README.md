# Factorial using Boost.Python and GMP
A simple calculation of factorial using Boost.Python and GMP

## Prerequisite
Requires Boost.Python and GMP. To install Boost.Python on Ubuntu, simply run:
```
apt-get install libboost-python-dev
apt-get install python-dev
```
## Compile
Simply run ``make``. This creates the file ``my_booster.so`` which is the shared object containing the module ``my_booster`` with the function ``factorial(n)``

## Run tests
Run ``./tests.py`` to compare execution speed of factorial using Boost.Python and GMP versus Python's ``math.factorial``

Example output:
```
======= my_booster =======
It took 1.796987 seconds to find factorial(133742)
Length of output in base 10: 627517

======= math.factorial =======
It took 3.863851 seconds to find factorial(133742)
Length of output in base 10: 627517

======= equality? =======
True 

======= speed up =======
2.15018302771 times faster
``` 
