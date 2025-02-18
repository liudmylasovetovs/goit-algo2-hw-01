def select_k_elem(arr, k):
    if not arr or k < 1 or k > len(arr):
        return None
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):
        return select_k_elem(left, k)
    elif k > len(arr) - len(right):
        return select_k_elem(right, k - (len(arr) - len(right)))
    else:
        return pivot
    
if __name__ == "__main__":
    test_list = [23, 5, 67, 12, 89, 45, 3, 56, 78, 1, 34, 99, 8, 20]
    print(select_k_elem(test_list, 3))