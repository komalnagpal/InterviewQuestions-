class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        nums.sort()
        for i in range(len(nums)):
            if ( i ==0 or (i > 0 and nums[i] != nums[i-1])): # Check for ignoring duplicate triplets
                lo = i+1
                hi = len(nums)-1
                while(lo < hi):
                    if (nums[lo] + nums[hi] == -nums[i]):
                        output.append([nums[i],nums[lo],nums[hi]])
                        while(lo < hi and nums[lo] == nums[lo+1]):
                            lo=lo + 1
                        while(lo < hi and nums[hi] == nums[hi - 1]):
                            hi = hi - 1
                        lo = lo +1
                        hi = hi -1 
                    elif (nums[lo] + nums[hi] < -nums[i]):
                        lo = lo + 1
                    else:
                        hi = hi - 1
        return output 
        
