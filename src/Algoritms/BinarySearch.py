from re import match

# O(log n)
# Работает только в отсортированной последовательности

def binary_search (nums, x):
    l = 0
    h = len(nums) - 1

    while l <= h:
        mid = (l + h) // 2
        gues = nums[mid]

        if gues == x:
            return mid
        if gues > x:
            h = mid - 1
        if gues < x:
            l = mid + 1
    return None

n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(binary_search(n, 6)) #