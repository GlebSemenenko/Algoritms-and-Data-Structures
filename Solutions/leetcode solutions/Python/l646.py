class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mp = {}
        duplicate = -1
        
        # Подсчитываем частоту каждого числа
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
            if mp[num] == 2:
                duplicate = num
        
        # Находим пропущенное число
        missing = -1
        for num in range(1, n + 1):
            if num not in mp:
                missing = num
                break
        
        return [duplicate, missing]