###########################################
# Author: Malay Agarwal
# Problem: 
# Given an array of integers, return a new 
# array such that each element at index i of
# the new array is the product of all the 
# numbers in the original array except the 
# one at i.
# ###########################################

def main():
    numList = [1,3,5,2,6]
    n = len(numList)
    left = [0]*n  
    right = [0]*n  
    prod = [0]*n  
    left[0] = 1
    right[n - 1] = 1
    for i in range(1, n):  
        left[i] = numList[i - 1] * left[i - 1]  
    for j in range(n-2, -1, -1):  
        right[j] = numList[j + 1] * right[j + 1]  
    for i in range(n):  
        prod[i] = left[i] * right[i]  
    for i in range(n):  
        print(prod[i], end =' ')  
main()