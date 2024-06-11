def is_anagram(str1, str2):
    """
    This function checks if two strings are anagrams.

    Args:
        str1: The first string.
        str2: The second string.

    Returns:
        True if the string are anagrams, otherwise False.
    """

    # Length check
    if len(str1) != len(str2):
        return False

    # Count characters in `str1`
    char_count = {}
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    # Match characters in `str2`
    for char in str2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True

print(is_anagram("silent", "listen")) # True
print(is_anagram("hello", "world")) # False
