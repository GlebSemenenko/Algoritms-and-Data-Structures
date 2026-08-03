def initialize_names(name):
    list = name.split()

    i = 1
    while i < len(list)-1:
        s = list[i]
        s = s[:1]
        s = s.upper()
        s = s + "."
        list[i] = s
        i += 1

    r = " ".join(list)
    return r

print(initialize_names('Alice Betty Catherine Davis'))