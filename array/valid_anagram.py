"""
Check if string 't' is an anagram of string 's'
"""


def is_anagram(s: str, t: str) -> bool:
    """Approach #1
    Time  O(nlogn)
    Space O(n)
    """
    return sorted(s) == sorted(t)


def is_anagram_2(s: str, t: str) -> bool:
    """
    Approach #2
    Time  O(n)
    Space O(n)
    """
    if len(s) != len(t):
        return False

    count = {}

    for i in s:
        count[i] = 1 + count.get(i, 0)

    for i in t:
        if i in count:
            count[i] -= 1
        else:
            return False

    return all(v == 0 for v in count.values())
