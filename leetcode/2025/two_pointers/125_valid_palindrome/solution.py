def isPalindrome1(s: str) -> bool:
    """
    Method 1 - Reverse string

    Time complexity:  O(n)
    Space complexity: O(n)
    """
    filtered_str = ""
    for ch in s:
        if ch.isalnum():
            filtered_str += ch.lower()
    return filtered_str == filtered_str[::-1]


def isPalindrome2(s: str) -> bool:
    """
    Method 2 - Two pointers

    Time complexity:  O(n)
    Space complexity: O(1)
    """
    l = 0
    r = len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return True


if __name__ == "__main__":
    inputs = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "",
    ]
    for i in inputs:
        res = isPalindrome1(i)
        print(res)
