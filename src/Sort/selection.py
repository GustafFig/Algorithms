def selection_sort(arr):
    i = 0

    while i < len(arr):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                # usign python to make an easy and legible positions change
                arr[i], arr[j] = arr[j], arr[i]
        i += 1

    return arr


# Insert in the begin and in the end of the array
def double_insertion_sort(arr):
    i = 0
    array_size = len(arr)
    while i < array_size // 2:
        end_i = array_size - i
        min_ind = i
        max_ind = i
        for j in range(i + 1, end_i):
            if arr[j] < arr[min_ind]:
                min_ind = j

            if arr[j] > arr[max_ind]:
                max_ind = j

        arr[min_ind], arr[i] = arr[i], arr[min_ind]
        arr[max_ind], arr[end_i - 1] = arr[end_i - 1], arr[max_ind]
        i += 1

    return arr


def recursive_insertion(arr, p=1):
    # only avoid an reduntant work to caller
    if p is None:
        p = len(arr) - 1

    if p == 0:
        return arr

    recursive_insertion(arr, p - 1)

    elem = arr[p]
    q = p - 1
    while elem < arr[q] and q >= 0:
        arr[q + 1] = arr[q]
        q -= 1

    arr[q + 1] = elem

    return arr

# its call it self, but only to pass to next number
# not create an recursive tree
def pseudo_recursive_insertion(arr, p=None):
    if p == len(arr):
        return arr

    elem = arr[p]
    q = p - 1

    while elem < arr[q] and q >= 0:
        arr[q + 1] = arr[q]
        q -= 1

    arr[q + 1] = elem

    return pseudo_recursive_insertion(arr, p + 1)


if __name__ == "__main__":
    entries = [
        [10, 12, 11, 1, 3, 4, 2, 5],
    ]
    for entrie in entries:
        # print(double_insertion_sort(entrie))
        print(recursive_insertion(entrie)
        # print(selection_sort(entrie))
