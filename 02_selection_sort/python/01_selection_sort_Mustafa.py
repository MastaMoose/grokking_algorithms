# -*- coding: utf-8 -*-
"""
Author: Mustafa
Description: This is Mustafa's attempt at a selection sort
    with smallets to largest sorting
"""
def find_smallest(A):
    smallest = A[0]
    smallPOS = 0
    for i in range(1, len(A)):
        if A[i] < smallest:
            smallest = A[i]
            smallPOS = i
        return smallPOS

def selection_sort(B):
    sorted = []
    #[smallest, smallPOS] = find_smallest(B)
    #sorted.append(B.pop(smallPOS))
    for i in range(0,len(B)):
    #while (len(B) != 0):
        #print(len(B))
        smallPOS = find_smallest(B)
        #print(smallPOS)
        sorted.append(B.pop(smallPOS))
        print(sorted)
        ##print(len(B))
    return sorted
    