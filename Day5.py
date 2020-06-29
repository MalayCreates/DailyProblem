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

def main(arr):
    temparr =[]
    for i in arr:
        if (i > 0) and (i not in temparr):
            temparr.append(i)
    for j in range(0,len(temparr)):
        if j != temparr[j]:
            return j
        else:
            return ('None')

main()