def min_max(arr):

    if not arr:
        return None, None

    if len(arr) == 1:
        return (arr[0], arr[0])

    mid = len(arr) // 2

    left_min, left_max = min_max(arr[:mid]) 
    right_min, right_max = min_max(arr[mid:]) 

    return (min(left_min, right_min), max(left_max, right_max))



if __name__ == "__main__":
    test_list = [23, 5, 67, 12, 89, 45, 3, 56, 78, 1, 34, 99, 8, 20]
    print(min_max(test_list))