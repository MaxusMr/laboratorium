# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:45:10 2023

@author: maxmr
"""

def porownaj(a,b,c):
    return(bool(a+b==c or a+b>=c))

f=int(input("Wprowadź liczbę "))
g=int(input("Wprowadź liczbę "))
h=int(input("Wprowadź liczbę "))
print(porownaj(f,g,h))