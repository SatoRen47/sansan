# -*- coding: utf-8 -*-
"""
Created on Thu May  9 19:32:57 2024

@author: USER
"""

for b in range(1, 10):
    for a in range(9, 1, -1):
        print(f"{a}*{b}={a*b}", sep="", end="\t")
    print()