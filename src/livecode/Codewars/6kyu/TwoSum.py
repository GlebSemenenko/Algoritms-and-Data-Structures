def two_sum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l != r:
        if numbers[l] + numbers[r] == target:
            return [l, r]
        elif numbers[l] + numbers[r] < target:
            l += 1
        elif numbers[l] + numbers[r] > target:
            r -=1
    return -1


print(two_sum([1,2,3,5],5))