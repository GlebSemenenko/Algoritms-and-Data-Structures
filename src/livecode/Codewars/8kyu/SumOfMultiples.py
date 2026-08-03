def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"

    # наибольшее число < m, кратное n
    last = ((m - 1) // n) * n
    if last < n:  # нет ни одного кратного
        return 0

    count = last // n  # сколько всего кратных
    return n * count * (count + 1) // 2
