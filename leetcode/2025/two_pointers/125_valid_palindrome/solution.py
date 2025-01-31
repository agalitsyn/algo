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
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
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
