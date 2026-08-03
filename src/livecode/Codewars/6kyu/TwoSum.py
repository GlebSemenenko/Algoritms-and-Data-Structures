def two_sum_sorted(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l != r:
        if numbers[l] + numbers[r] == target:
            return l, r
        elif numbers[l] + numbers[r] < target:
            l += 1
        elif numbers[l] + numbers[r] > target:
            r -=1
    return -1


def two_sum(numbers, target):
    for i in range (len(numbers)):
        for j in range (len(numbers)):
            if numbers[i] + numbers[j] == target:
                if i == j:
                    continue
                return i, j
    return -1