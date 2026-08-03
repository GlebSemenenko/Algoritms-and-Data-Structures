def remove_smallest(numbers):
    res = []
    if len(numbers) == 0:
        return res
    min = numbers[0]
    c = 0
    for num in range(len(numbers)):
        if numbers[num] < min:
            min = numbers[num]
    print(min)
    for num in range(len(numbers)):
        if numbers[num] == min and c == 0:
            c += 1
            continue
        res.append(numbers[num])
    return res

print(remove_smallest([1, 2, 3, 4, 5]))
