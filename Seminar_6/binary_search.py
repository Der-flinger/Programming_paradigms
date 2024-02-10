
def binary_search(array, find_el, min_index = 0, max_index = None) -> int:

    if max_index is None:
        max_index = len(array) - 1

    if min_index <= max_index:
        mid_index = (min_index + max_index) // 2

        if find_el == array[mid_index]:
            print(f"Элемент равный {find_el} находится под индексом {mid_index}")
            return mid_index
        elif find_el < array[mid_index]:
            return binary_search(array, find_el, min_index, mid_index - 1)
        elif find_el > array[mid_index]:
            return binary_search(array, find_el, mid_index + 1, max_index)
    return -1

arr = [1, 2, 3 ,6,213,43,78,9786,5,21,45,7,4,24]
arr.sort()
print(arr)
result = binary_search(arr, 45)
print(result)

# def binary_search(array, find_el, start=0, end=None) -> int:
#     if end is None:
#         end = len(array) - 1

#     if start <= end:
#         mid = (start + end) // 2
#         mid_element = array[mid]

#         if find_el == mid_element:
#             print(f"Элемент равный {mid_element} находится под индексом {mid}")
#             return mid
#         elif find_el < mid_element:
#             return binary_search(array, find_el, start, mid - 1)
#         else:
#             return binary_search(array, find_el, mid + 1, end)

#     return -1