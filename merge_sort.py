# also just a Wikipedia implementation


def merge_sort(m: list) -> list:
    list_length = len(m)
    if list_length <= 1:
        return m

    left, right = [], []

    half_point = list_length // 2
    for i, item in enumerate(m):
        if i < half_point:
            left.append(item)
            continue
        right.append(item)

    return merge(merge_sort(left), merge_sort(right))


def merge(left: list, right: list) -> list:
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    result += left + right

    return result
