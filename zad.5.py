# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:45:36 2023

@author: maxmr
"""

def zawiera(a,b):
    return(bool(b in a))


l=[3,6,9,15,26,27,97,4,83,20,74,37,17,268,36,375]
i=int(input("Wprowadź liczbę "))
print(zawiera(l,i))
