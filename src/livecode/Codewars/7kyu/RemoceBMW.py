# Remove BMW 7
def remove_bmw(string):
    black_list = "bmwBMW"
    for ch in string:
        if ch in black_list:
            string = string.replace(ch, "")
    return string