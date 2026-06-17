class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = len(nums)
        count = 0
        p = 0
        for i in range (l):
            if nums[i] == 1:
                p+=1
            else :
                p = 0
            if p > count:
                count = p
        return count