# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 22:59:01 2018

@author: MastaMoose
"""

def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0]+sum(arr[1:])
    
def count_list(A):
    if A == []:
        return 0
    else:
        return 1 + count_list(A[1:])
    
def max_list(A):
    Max = A[0]
    if len(A) == 2:
        if A[1] >= A[0]:
            Max = A[1]
        else:
            pass
    else:
        if max_list(A[1:]) >= Max:
            Max = max_list(A[1:])
        else:
            pass
    return Max

def binary_search(A, item):
    low = 0
    high = len(A) - 1
    mid = (low + high) // 2
    guess = A[mid]
    if guess == item:
        return mid
    elif guess > item:
        binary_search(A[:mid], item)
    else:
        binary_search(A[mid+1:], item)

def quicksort(A):
    if len(A) < 2:
        return A
    else:
        pivot = A[0]
        less = [i for i in A[1:] if i <= pivot]
        greater = [i for i in A[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
        
def multiply_array(A):
    B = []
    for i in A:
        for j in A:
            B.append(i*j)
    return B, len(B)

def multiply_array2(A):
    B = [i*j for i in A for j in A]
    return B, len(B)