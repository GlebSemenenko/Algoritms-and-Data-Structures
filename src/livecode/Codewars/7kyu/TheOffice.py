def outed(meet, boss):
    count = 0
    res = 0
    for k, v in meet.items():
        if k == boss:
            v = v * 2
        count += 1
        res += v
    return res / count