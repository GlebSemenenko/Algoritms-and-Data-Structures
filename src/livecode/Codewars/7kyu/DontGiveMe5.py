def dont_give_me_five(start,end):
    res = end - start + 1
    print(res)
    for n in range (start, end + 1):
        if "5" in str(n):
            print(n, "find")
            res -= 1
    return res