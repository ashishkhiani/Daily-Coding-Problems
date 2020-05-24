def find_nearest_larger_number(arr, index):
    i = 1
    number = arr[index]

    while i != len(arr):
        # check left of index
        left = index - i
        if left >= 0 and arr[left] > number:
            return left

        # check right of index
        right = index + i
        if right < len(arr) and arr[right] > number:
            return right

        i += 1

    return None
