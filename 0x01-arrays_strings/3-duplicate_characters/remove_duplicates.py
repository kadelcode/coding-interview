"""
A module containing the `remove_duplicates`
function along with test cases.
"""


def remove_duplicates(string):
    """
    Removes duplicate characters from a string
    without using any additional buffer
    
    Args:
        string: The string to remove duplicates from.

    Returns:
        The string with duplicates removed.
    """

    j = 0
    
    # convert string to list for in-place modification
    string = list(string)

    for i in range(len(string)):
        if i == 0 or string[i] != string[i - 1]:
            string[j] = string[i]
            j += 1
    return ''.join(string[:j])

# Test cases
print(remove_duplicates("hello")) # Output: "helo"
print(remove_duplicates("aabbcc")) # Output: "abc"
print(remove_duplicates("abc")) # Output: "abc"
print(remove_duplicates("")) # Output: ""
print(remove_duplicates("aabbaccc")) # Output: "abc"
print(remove_duplicates("football")) # Output: "fotbal"
