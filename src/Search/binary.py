def binary_search(arr, elem):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < elem:
            low = mid + 1
        elif arr[mid] > elem:
            high = mid
        else:  # arr[mid] == elem
            return mid
    return -1

def recursive_binary_tree(arr, elem, low, high):
    mid = (low + high) // 2
    if low == high:
        return -1

    if arr[mid] < elem:
        low = mid + 1
    elif arr[mid] > elem:
        high = mid
    else:
        return mid
    
    return recursive_binary_tree(arr, elem, low, high)


if __name__ == "__main__":
    entries = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11),
    ]
    for arr, elem in entries:
        print(recursive_binary_tree(arr, elem, 0, len(arr)))
