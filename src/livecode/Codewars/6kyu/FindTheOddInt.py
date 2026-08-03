
def find_it(seq):
    mp = {}
    for n in seq: # Проверить кол-во вхождений каждого числа
        if n in mp:
            mp[n] += 1
        else:
            mp[n] = 1
    for k, v in mp.items():
        if v % 2 != 0:
            return k
    return -1