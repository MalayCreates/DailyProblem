###########################################
# Author: Malay Agarwal
# Problem: 
# Given an array of integers A sorted in
# non-decreasing order, return an array of 
# the squares of each number, also in sorted
# non-decreasing order.
# ###########################################


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        for i in range(len(A)):
            A[i] = (A[i]) ** 2
        A.sort()
