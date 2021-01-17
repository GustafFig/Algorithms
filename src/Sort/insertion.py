import random

def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]

        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1

        arr[i + 1] = key
    return arr


# To strug the emotion of this algorith, if we alwais put the average of the current elements
# in the array, the next average will be the same. So it's the same append the same number in arr
def medium_case_creator(length=10, min_value=1, max_value=100):
    arr = []

    first_elem = random.randint(min_value, max_value);
    second_elem = random.randint(min_value, max_value);

    arr.append(first_elem)
    arr.append(second_elem)

    i = 2
    avg = (first_elem + second_elem) // i
    print(avg)
    while i < length:
        arr.append(avg)
        i += 1
        print(avg)
    return arr

if __name__ == "__main__":
    entries = [
        [10, 12, 11, 1, 3, 4, 2, 5],
    ]
    for entrie in entries:
        print(insertion_sort(entrie))

    print(medium_case_creator())
