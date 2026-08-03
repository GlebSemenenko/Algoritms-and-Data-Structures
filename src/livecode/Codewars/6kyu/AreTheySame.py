# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

def comp(array1, array2) -> bool:
    if array1 is None or array2 is None:
        return False

    if len(array1) != len(array2):
        return False

    mp1 = {}
    mp2 = {}

    for x in array1:
        mp1[x] = mp1.get(x, 0) + 1

    for x in array2:
        mp2[x] = mp2.get(x, 0) + 1

    for x in mp1:
        p = x * x
        if p not in mp2:
            return False
        if mp2[p] != mp1[x]:
            return False

    return True






