# -*- coding: utf-8 -*-
"""
Created on Thu May  9 19:32:06 2024

@author: USER
"""

a = 0
num = 0
b = []

for i in range(1, 101):
    if 1 % 2 == 1:
        a += i

    if i % 7 == 0:
        num += i
        
    if i % 5 == 0 and i % 15 == 0:
        b.append(i)
        
print(f"奇數和為:{a}")
print(f"可被7整除的數總和為:{num}")
print(f"可被5和15整除的數為{b}")