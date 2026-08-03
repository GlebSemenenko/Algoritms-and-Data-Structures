def narcissistic( value ):
    str_value = str(value)
    l = len(str_value)
    n = 0
    for ch in str_value:
        n += pow(int(ch), l)
    if n == value:
        return True
    return False