# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 18:00:48 2019

@author: Zhaobin
"""

from fib import fib

def test_fib():
    assert fib(2) == 1
    assert fib(5) == 5
    assert fib(12) == 144