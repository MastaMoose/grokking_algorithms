# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 19:26:21 2018

@author: MastaMoose
"""

def countdown(N):
    print(N)
    if N == 0:
        return
    else:
        countdown(N-1)
        
def fact(N):
    if N == 1:
        return 1
    else:
        return N*fact(N-1)