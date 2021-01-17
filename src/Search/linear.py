
"""
For invariant loop, we have,
invariant: the searcheds values, not returned, aren't the element we are looking for
Init: any value have been searched, so the invariant is true
Maintance: the all values < i have been evaluated like different of elem, and if arr[i]
too, in the next loop the invariant continue been true
Final: In the end or all the values have been evaluated, or we found the value and return
it so. Then the invariant cnotinue be truthy
"""

def linear_search(arr, elem):
    for i in range(len(arr)):
        if arr[i] == elem:
            return i

    return None

if __name__ == "__main__":
    entries = [
        ([1, 2, 3, 4, 5, 6, 7, 8], 7),
    ]
    for entrie_arr, entrie_elem in entries:
        print(linear_search(entrie_arr, entrie_elem))
        print(entrie_arr[linear_search(entrie_arr, entrie_elem)] == entrie_elem)
