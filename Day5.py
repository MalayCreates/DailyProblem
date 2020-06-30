###########################################
# Author: Malay Agarwal
# Problem: 
# Given an array of integers, find the first 
# missing positive integer in linear time 
# and constant space. In other words, find 
# the lowest positive integer that does not 
# exist in the array. The array can contain 
# duplicates and negative numbers as well.
# ###########################################
r = [1,2,0,3,6,4]
def main(arr):
    m = max(arr)
    if m < 1: 
        return 1 
    if len(arr) == 1: 
        return 2 if arr[0] == 1 else 1     
    l = [0] * m 
    for i in range(len(arr)): 
        if arr[i] > 0: 
            if l[arr[i] - 1] != 1: 
                l[arr[i] - 1] = 1 
    for i in range(len(l)): 
        if l[i] == 0:  
            return i + 1
    return i + 2    

arr = [0, 10, 2, -10, -20] 

print(main(arr)) 