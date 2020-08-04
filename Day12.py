###########################################
# Author: Malay Agarwal
# Problem: 
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes 
# along the longest path from the root node 
# down to the farthest leaf node.
###########################################

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leftmost = self.maxDepth(root.left)
        rightmost = self.maxDepth(root.right)
        maxdepth = max(leftmost, rightmost)
        return maxdepth