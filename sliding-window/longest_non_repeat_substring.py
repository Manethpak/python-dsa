def non_repeat_substring(string) -> int:
    longest = 0
    seen = {}
    window_start = 0

    for window_end in range(len(string)):
        right = string[window_end]
        if right in seen:
            window_start = max(window_start, seen[right] + 1)
        seen[right] = window_end
        longest = max(longest, window_end - window_start + 1)

    return longest
