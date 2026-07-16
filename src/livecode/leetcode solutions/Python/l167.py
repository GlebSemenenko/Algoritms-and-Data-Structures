def twoSum(numbers: List[int], target: int) -> List[int]:
    res = []

    l = 0
    r = len(numbers) - 1

    while l < r:
        answer = numbers[l] + numbers[r]
        if answer > target:
            r -= 1
        if answer < target:
            l += 1
        if answer == target:
            res.append(l + 1)
            res.append(r + 1)
            return res
    return res

numbers = [2,7,11,15]
target = 9

print(twoSum(numbers, target))
