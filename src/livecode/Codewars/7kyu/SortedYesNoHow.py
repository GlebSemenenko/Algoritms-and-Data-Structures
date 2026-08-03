def is_sorted_and_how(arr):
    if len(arr) <= 1:
        return "yes, ascending"

    asc = True
    desc = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            asc = False
        if arr[i] > arr[i - 1]:
            desc = False

    if asc:
        return "yes, ascending"
    elif desc:
        return "yes, descending"
    else:
        return "no"
