# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 14:57:41 2017

@author: t0tem
"""

#%%

x = 0
for i in range(int(input())):
    x += int(input())
print(x)

#%%


print(sum([int(input()) for i in range(int(input()))]))
print(sum(int(input()) for i in range(int(input()))))


x = (int(input()) for i in range(int(input())))
x

#%%

x = [1,2,3]
id(x)
id([1,2,3])
y = x
y is x
y is [1,2,3]
type(x)
input()

