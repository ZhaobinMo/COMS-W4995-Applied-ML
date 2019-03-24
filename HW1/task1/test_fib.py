# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 18:00:48 2019

@author: Zhaobin
"""

from fib import fib

def test_fib():
    assert ((fib(2) == 1)&(fib(5) == 5)&(fib(12) == 144))