# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 17:52:22 2019

@author: Zhaobin
"""

def fib(n):
    """return the result of the Fibonacci sequence
    """
    f_n_1 = 0
    f_n = 1
    for i in range(n):
        f_n, f_n_1 = f_n_1, f_n+f_n_1
    return f_n_1