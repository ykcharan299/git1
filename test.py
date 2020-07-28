# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:37:13 2019

@author: ykcha
"""

import pandas as pd

import numpy as np



z = np.arange(10, 16)

s = pd.Series(z, index=list('abcdef'))



#Accessing 3rd element of s.

print (s[2]) # ---> Returns '12' 



#Accessing 4th element of s.

print(s['d']) # ---> Returns '13'

print(s[1:4])
print(s['b':'e'])