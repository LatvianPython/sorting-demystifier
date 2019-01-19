# recreated from a picture from stack overflow

def sort(a: list):
    list_length = len(a)
    for i in range(list_length):

        current_value = a[i]

        smallest = (i, current_value)
        for j in range(i + 1, list_length):
            if a[j] < smallest[1]:
                smallest = (j, a[j])

        a[i], a[smallest[0]] = smallest[1], current_value
