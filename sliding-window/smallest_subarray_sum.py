def smallest_subarray_sum(s, arr) -> int:
    """
    Find the length of the smallest contiguous subarray whose sum is greater than or equal to 's'.
    Time  O(n)
    Space O(1)
    """
    min_index = float('inf')
    window_start = 0
    window_sum = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_index = min(min_index, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_index == float('inf'):
        return 0
    return min_index
