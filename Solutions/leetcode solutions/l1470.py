class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        l = len(nums)
        ll = int(l / 2)
        for i in range (ll):
            res.append(nums[i])
            res.append(nums[ll + i])
        return res
