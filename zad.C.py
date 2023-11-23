# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 13:51:40 2023

@author: maxmr
"""

def par(lista):
  for el in lista:
    if el%2==0:
      print(el)


l=list(range(1,11))
par(l)
