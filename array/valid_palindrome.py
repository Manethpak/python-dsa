"""
Check if string 's' is a valid palindrome
"""


def is_palindrome(s: str) -> bool:
    """Approach #1
    Time  O(n)
    Space O(n)
    """
    s = "".join([i.lower() for i in s if i.isalnum()])
    return s == s[::-1]


def is_palindrome_2(s: str) -> bool:
    """
    Approach #2
    Time  O(n)
    Space O(n)
    """
    s = "".join([i.lower() for i in s if i.isalnum()])
    l, r = 0, len(s)-1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True
