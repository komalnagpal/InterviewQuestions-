# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.minimalTree(0,len(nums)-1,nums)
        
    def minimalTree(self,start,end,nums):
        if start > end:
            return None
        mid = (start+end)/2
        root = TreeNode(nums[mid])
        root.left = self.minimalTree(start,mid-1,nums)
        root.right = self.minimalTree(mid+1,end,nums)
        return root
        
        
