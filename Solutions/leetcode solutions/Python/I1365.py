class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            count = 0
            for item in nums:
                if item < i:
                    count += 1
            res.append(count)
        return res