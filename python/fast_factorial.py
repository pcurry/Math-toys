
"""
A collection of Python implementations of fast factorial algorithms 
discussed on the Fast Factorial website: http://www.luschny.de/math/factorial/FastFactorialFunctions.htm

I learned the algorithms by looking at his code, but I wrote all 
the Python here myself.
"""

import math

def naive(num):
    """
    The naive factorial algorithm.  Here mostly for comparison.
    """
    if num in (0, 1):
        return 1
    else:
        return num * naive(num - 1)


def moessner(num):
    """
    Very slow algorithm that uses only addition.  Cool but impractical.

    Based on the C# code here: http://www.luschny.de/math/factorial/csharp/FactorialAdditiveMoessner.cs.html
    """
    s = [ 0 for x in xrange(num + 1) ]
    s[0] = 1
    for m in xrange(num):
        m += 1
        k = m
        while (k >= 1):
            for i in xrange(k):
                i += 1
                s[i] += s[i - 1] 
            k -= 1
    return s[num]
