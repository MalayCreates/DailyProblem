###########################################
# Author: Malay Agarwal
# Problem: 
# Given an array, rotate the array to the 
# right by k steps, where k is non-negative.
# ###########################################
r = [1,2,3,4,5]
s = 2
def main(arr,k):
    temparr = arr[-k:]
    temparr += arr[:k+1]
    print(temparr)
main(r,s)