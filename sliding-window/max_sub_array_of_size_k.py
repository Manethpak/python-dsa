def max_sub_array_of_size_k(k, arr) -> int:
    """
    find the maximum sum of any contiguous subarray of size 'k'.
    Time  O(n)
    Space O(1)
    """
    max_sum = 0
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum
