def split_string( string ):
    result = []
    if len(string) % 2 != 0:
        string += "_"

    for i in range(0, len(string), 2):
        appended = string[i] + string[i+1]
        result.append(appended)
    return result