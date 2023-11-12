# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:44:42 2023

@author: maxmr
"""

def parzysta(a):
    b=bool(a%2==0)
    if b==True:
        return("Liczba przysta")
    else:
        return("Liczba nieprazysta")
    
e=int(input("Wprowadź liczbę "))
print(parzysta(e))